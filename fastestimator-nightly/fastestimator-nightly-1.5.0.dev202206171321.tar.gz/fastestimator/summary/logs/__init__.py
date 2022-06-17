# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
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
from typing import TYPE_CHECKING

import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach(__name__,
                                            submod_attrs={
                                                'log_parse': ['parse_log_dir', 'parse_log_file', 'parse_log_files'],
                                                'log_plot': ['plot_logs', 'visualize_logs'],
                                            })

if TYPE_CHECKING:
    from fastestimator.summary.logs.log_parse import parse_log_dir, parse_log_file, parse_log_files
    from fastestimator.summary.logs.log_plot import plot_logs, visualize_logs
