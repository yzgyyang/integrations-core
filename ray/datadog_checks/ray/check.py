# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from random import random, randint

from datadog_checks.base import OpenMetricsBaseCheckV2
from datadog_checks.ray.config_models import ConfigMixin

from .metrics import METRIC_MAP


class RayCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = 'ray'
    DEFAULT_METRIC_LIMIT = 0

    def __init__(self, name, init_config, instances=None):
        super().__init__(name, init_config, instances)
        self.bytes = 100

    def check(self, instance):
        super().check(instance)
        self.gauge('node.gpus_utilization', randint(0, 100))
        self.gauge('node.gram_used', self.bytes)
        self.bytes += 200

    def get_default_config(self):
        return {
            "metrics": [METRIC_MAP],
        }
