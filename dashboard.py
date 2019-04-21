# encoding: utf-8

from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.utils import get_admin_site_name
from jet.dashboard.dashboard_modules import google_analytics




class CustomIndexDashboard(Dashboard):
    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js', 'admin/js/jquery.init.js')