# Copyright (c) 2021, NVIDIA CORPORATION.
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

import pytest

from data_gen import *
from asserts import assert_gpu_and_cpu_are_equal_collect

allow_collect_conf={"spark.rapids.sql.exec.CollectLimitExec": "true"}

@pytest.mark.parametrize('data_gen', all_gen)
def test_collect_limit(data_gen):
    assert_gpu_and_cpu_are_equal_collect(lambda spark: unary_op_df(spark, data_gen, length=2048).limit(2048),
                                         allow_collect_conf)

