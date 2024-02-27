METRIC_MAP = {
    'analysis_run_info': 'analysis.run.info',
    'analysis_run_metric_phase': 'analysis.run.metric.phase',
    'analysis_run_metric_type': 'analysis.run.metric.type',
    'analysis_run_phase': 'analysis.run.phase',
    'analysis_run_reconcile': 'analysis.run.reconcile',
    'analysis_run_reconcile_error': 'analysis.run.reconcile.error',
    'argo_rollouts_controller_info': 'conroller.info',
    'controller_clientset_k8s_request': 'controller.clientset.k8s.request',
    'experiment_info': 'experiment.info',
    'experiment_phase': 'experiment.phase',
    'experiment_reconcile': 'experiment.reconcile',
    'experiment_reconcile_error': 'experiment.reconcile.error',
    'go_gc_duration_seconds': 'go.gc.duration.seconds',
    'go_goroutines': 'go.goroutines',
    'go_info': 'go.info',
    'go_memstats_alloc_bytes': {'name': 'go.memstats.alloc_bytes', 'type': 'native_dynamic'},
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck.hash.sys.bytes',
    'go_memstats_frees': 'go.memstats.frees',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc.sys.bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap.alloc.bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap.idle.bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap.inuse.byes',
    'go_memstats_heap_objects': 'go.memstats.heap.objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap.released.bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap.sys.bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last.gc.time.seconds',
    'go_memstats_lookups': 'go.memstats.lookups',
    'go_memstats_mallocs': 'go.memstats.mallocs',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache.inuse.bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache.sys.bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan.inuse.bytes',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan.sys.bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next.gc.bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other.sys.bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack.inuse.bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack.sys.bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys.bytes',
    'go_threads': 'go.threads',
    'notification_send': 'notification.send',
    'process_cpu_seconds': 'process.cpu.seconds',
    'process_max_fds': 'process.max.fds',
    'process_open_fds': 'process.open.fds',
    'process_resident_memory_bytes': 'process.resident.memory.bytes',
    'process_start_time_seconds': 'process.start.time.seconds',
    'process_virtual_memory_bytes': 'process.virtual.memory.bytes',
    'process_virtual_memory_max_bytes': 'process.virtual.memory.max.bytes',
    'rollout_events': 'rollout.events',
    'rollout_info': 'rollout.info',
    'rollout_info_replicas_available': 'rollout.info.replicas.available',
    'rollout_info_replicas_desired': 'rollout.info.replicas.desired',
    'rollout_info_replicas_unavailable': 'rollout.info.replicas.unavailable',
    'rollout_info_replicas_updated': 'rollout.info.replicas.updated',
    'rollout_phase': 'rollout.phase',
    'rollout_reconcile': 'rollout.reconcile',
    'rollout_reconcile_error': 'rollout.reconcile.error',
    'workqueue_adds': 'workqueue.adds',
    'workqueue_depth': 'workqueue.depth',
    'workqueue_longest_running_processor_seconds': 'workqueue.longest.running.processor.seconds',
    'workqueue_queue_duration_seconds': 'workqueue.queue.duration.seconds',
    'workqueue_retries': 'workqueue.retries',
    'workqueue_unfinished_work_seconds': 'workqueue.unfinished.work.seconds',
    'workqueue_work_duration_seconds': 'workqueue.work.duration.seconds'
}

RENAME_LABELS_MAP = {
    "name": "argo_rollout_name",
    'namespace': 'argo_rollout_namespace',
}