from distutils.log import INFO, info
from django.shortcuts import render


import logging
logger = logging.getLogger(__name__)

# Create your views here.
def helloworldfunction(request):

    logger.debug('kt_debug.log')
    logger.info('kt_info.log')
    logger.warning('kt_warning.log')
    logger.error('kt_error.log')
    logger.critical('kt_critical.log')

    logger.error(__name__)

    return render(request, 'accounts/index.html')

