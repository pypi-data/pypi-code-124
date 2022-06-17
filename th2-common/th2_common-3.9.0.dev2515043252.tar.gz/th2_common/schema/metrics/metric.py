#   Copyright 2022 Exactpro (Exactpro Systems Limited)
#   Copyright 2021-2022 Exactpro (Exactpro Systems Limited)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from abc import ABC


class Metric(ABC):

    def is_enabled(self) -> bool:
        """
        Checks if status of a monitor is `enabled`

        :return: Status (bool) of MetricMonitor
        """
        pass

    def enable(self) -> None:
        """
        Changes status of a monitor to `enabled`

        """
        pass

    def disable(self) -> None:
        """
        Changes status of a monitor to `disabled`

        """
        pass
