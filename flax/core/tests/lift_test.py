# Copyright 2020 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flax.core import Scope, init, apply, lift

from jax import random
from jax import numpy as jnp

import numpy as np


from absl.testing import absltest

class ScopeTest(absltest.TestCase):

  def test_aliasing(self):
    def f(scope):
      a = scope.push('a')

      def g(scopes, _):
        scope, a = scopes
        self.assertEqual(a.parent, scope)
      
      lift.vmap(g, variable_in_axes={}, variable_out_axes={}, split_rngs={})((scope, a), jnp.ones((1,)))

    init(f)(random.PRNGKey(0))

  


if __name__ == '__main__':
  absltest.main()
