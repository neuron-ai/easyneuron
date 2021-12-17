# Copyright 2021 Neuron-AI GitHub Authors. All Rights Reserved.
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
# ==============================================================================
from random import normalvariate
from secrets import randbelow
from typing import Tuple

from numpy import array, ndarray


def gen_stairs(classes: int, features: int, samples: int = 10000, sd: float = 0.3, factor: float = 3) -> Tuple[ndarray, ndarray]:
    X = []
    y = []

    for _ in range(samples):
        label = randbelow(classes)*factor
        to_append = [normalvariate(label, sd) for _ in range(features)]

        X.append(to_append)
        y.append(label)

    return array(X), array(y)