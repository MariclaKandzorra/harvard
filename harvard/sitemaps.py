from todo.sitemaps import StaticSitemap, TaskListViewSitemap, TaskViewSitemap

sitemaps = {
    'static': StaticSitemap,
    'tasklists': TaskListViewSitemap,
    'tasks': TaskViewSitemap,
}