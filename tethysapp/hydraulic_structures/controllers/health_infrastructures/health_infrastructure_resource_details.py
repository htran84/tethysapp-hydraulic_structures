"""
* Name: model_resource_details.py
* Author: msouffront, htran
* Created On: January 26, 2021
* Copyright: (c) Aquaveo 2021
********************************************************************************
"""
__all__ = ['HydraulicStructuresHealthInfrastructureResourceDetails']

from tethysext.atcore.controllers.resources import TabbedResourceDetails
from tethysapp.hydraulic_structures.controllers.health_infrastructures.tabs import HealthInfrastructureFilesTab, HealthInfrastructureSummaryTab


class HydraulicStructuresHealthInfrastructureResourceDetails(TabbedResourceDetails):
    """
    Controller for Model details page(s).
    """
    base_template = 'hydraulic_structures/base.html'
    tabs = (
        {'slug': 'summary', 'title': 'Summary', 'view': HealthInfrastructureSummaryTab},
        {'slug': 'files', 'title': 'Files', 'view': HealthInfrastructureFilesTab},
    )
