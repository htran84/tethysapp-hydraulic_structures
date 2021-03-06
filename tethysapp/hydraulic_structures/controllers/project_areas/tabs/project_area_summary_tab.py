"""
********************************************************************************
* Name: project_area_summary_tab.py
* Author: gagelarsen
* Created On: December 02, 2020
* Copyright: (c) Aquaveo 2020
********************************************************************************
"""
from tethysext.atcore.controllers.resources import ResourceSummaryTab
from tethysext.atcore.mixins.file_collection_controller_mixin import FileCollectionsControllerMixin

from tethysapp.hydraulic_structures.services.spatial_managers.hydraulic_structures import HydraulicStructuresProjectAreaSpatialManager

from tethysapp.hydraulic_structures.services.map_manager import HydraulicStructuresMapManager


class ProjectAreaSummaryTab(ResourceSummaryTab, FileCollectionsControllerMixin):
    has_preview_image = True
    preview_image_title = "Extent"

    def get_map_manager(self):
        return HydraulicStructuresMapManager

    def get_spatial_manager(self):
        return HydraulicStructuresProjectAreaSpatialManager

    def get_summary_tab_info(self, request, session, resource, *args, **kwargs):
        """
        Define specific summary info.
        """
        # Tab layout
        column1 = []  # Auto-populated with default extent and description
        column2 = []

        tab_content = [column1, column2]

        # Generate summary of the models and hydraulic_infrastructures associated with this irrigation zone
        md_summary = ('Related Resources', {
            'Workflows': len(resource.workflows),
            'Hydraulic Infrastructures': len(resource.hydraulic_infrastructures),
        })
        column2.append(md_summary)

        # Generate summary about file collections and add to column 2
        fc_details = self.get_file_collections_details(session, resource)
        column2.extend(fc_details)

        return tab_content

    def get_preview_image_url(self, request, resource, *args, **kwargs):
        """
        Get URL from GeoServer that will generate a PNG of the default layers.
        """

        gs_engine = self.get_app().get_spatial_dataset_service(self.get_app().GEOSERVER_NAME, as_engine=True)
        spatial_manager = self.get_spatial_manager()(geoserver_engine=gs_engine)
        layer_preview_url = spatial_manager.get_resource_extent_wms_url(resource=resource)

        return layer_preview_url
