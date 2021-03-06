#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
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

# TODO: define framework api 
from paddle.fluid.layer_helper_base import LayerHelperBase
from paddle.fluid.data_feeder import convert_dtype

__all__ = ['set_default_dtype', 'get_default_dtype']


def set_default_dtype(d):
    """
    Set default dtype. The default dtype is initially float32

    Args:
        d(string|np.dtype): the dtype to make the default

    Returns:
        None.

    Examples:
        .. code-block:: python

            import paddle
            paddle.set_default_dtype("float32")

    """
    d = convert_dtype(d)
    LayerHelperBase.set_default_dtype(d)


def get_default_dtype():
    """
    Get the current default dtype. The default dtype is initially float32

    Args:
        None.
    Returns:
        The default dtype.

    Examples:
        .. code-block:: python

            import paddle
            paddle.get_default_dtype()
    """
    return LayerHelperBase.get_default_dtype()
