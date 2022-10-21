# Airflow Trigger Rules

By default, all tasks have the same trigger rule **all_success** set which meas, if all parents of a task succeed, then the task gets triggerd.

Only one trigger rule at a time can be specified for a given task.



## all_success

This one is pretty straightforward, and you've already seen it, your task gets triggered when all upstream tasks have succeeded.

One caveat though, if one of the parents gets skipped, then the task gets skipped as well as shown below.



## all_failed

Pretty clear, your task gets triggered if all of its parent tasks have failed.

Like with all_success, it Task B gets skipped, Task C gets skipped as well.



## all_done

You just want to trigger your task once all upstream tasks are done with their execution whatever their state.

This tirgger rule might be useful if there is a task that you always want to execute regardless of the upstream task's states



## one_failed

As soon as one of the upstream tasks fails, your task gets triggerd.

Can be useful if you have some long running tasks and want to do something as soon as one fails.



## one_success

Like with one_failed, but the opposite. As soon as one of the upstream tasks succeeds, your task gets triggered.



## none_failed

Your task gets triggered if all upstream tasks have **succeeded** or been **skipped**.

Only useful if you want to handle the skipped status.



## none_failed_min_one_success

Before known as "none_failed_or_skipped" (before Airflow 2.2), with this trigger rule, your task gets triggered if all upstream tasks haven't failed and at least one has succeeded.



## none_skipped

With this simple tirgger rule, your task gets triggered if no upstream tasks are skipped. If they are all in success or failed



## Conclusion

Airflow trigger rules are simple to use but yet, extremely powerful. They allow you to make more complex data pipelines and address real use cases. Don't hesitate ot use them in order to handle error in a better more reliable way that just with a callback.