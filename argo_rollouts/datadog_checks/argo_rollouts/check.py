# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base import OpenMetricsBaseCheckV2  # noqa: F401

from .metrics import METRIC_MAP, RENAME_LABELS_MAP


class ArgoRolloutsCheck(OpenMetricsBaseCheckV2):
    DEFAULT_METRIC_LIMIT = 0
    __NAMESPACE__ = 'argo_rollouts'

    def __init__(self, name, init_config, instances=None):

        super(ArgoRolloutsCheck, self).__init__(
            name,
            init_config,
            instances,
        )

    def get_default_config(self):
        return {
            'metrics': [METRIC_MAP],
            "rename_labels": RENAME_LABELS_MAP,
        }
