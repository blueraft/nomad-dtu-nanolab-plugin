#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import TYPE_CHECKING

import numpy as np
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import BrowserAnnotation
from nomad.datamodel.metainfo.basesections import CompositeSystem
from nomad.metainfo import MEnum, Package, Quantity, Section

from nomad_dtu_nanolab_plugin.categories import DTUNanolabCategory

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='DTU customised Substrate scheme')


class DTUSubstrate(CompositeSystem, Schema):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[DTUNanolabCategory],
        label='Substrate',
    )
    supplier_id = Quantity(
        type=str,
        default = 'Siegert Wafer',
        a_eln={'component': 'StringEditQuantity'},
    )
    substrate_polishing = Quantity(
        type=MEnum(['1 sided', '2 sided', 'none']),
        default = '1 sided',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    doping_type_of_substrate = Quantity(
        type=MEnum(['n', 'p', 'none']),
        default = 'n',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    doping_of_substrate = Quantity(
        type=np.float64,
        description="""
            The doping of the substrate measured as the electrical resistivity.
        """,
        default = 0.2,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm',},
        unit='(kg*m^3)/(A^2*s^3)',
    )
    doping_elements = Quantity(
        type=str,
        default = 'P',
        a_eln={'component': 'StringEditQuantity'},
    )
    length = Quantity(
        type=np.float64,
        default = 0.04,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='m',
    )
    width = Quantity(
        type=np.float64,
        default = 0.04,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='m',
    )
    thickness = Quantity(
        type=np.float64,
        default = 0.000675,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='m',
    )
    substrate_history = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    edx_data_file = Quantity(
        type=str,
        a_browser=BrowserAnnotation(adaptor='RawFileAdaptor'),
        a_eln={'component': 'FileEditQuantity', 'label': 'EDX file'},
    )
    avg_S = Quantity(
        type=np.float64,
        description="""
            The average S atomic percent from the EDX measurement
                            """,
        a_eln={'component': 'NumberEditQuantity'},
    )
    avg_P = Quantity(
        type=np.float64,
        description="""
            The average P atomic percent from the EDX measurement
                            """,
        a_eln={'component': 'NumberEditQuantity'},
    )
    avg_M1 = Quantity(
        type=np.float64,
        description="""
            The average M1 atomic percent from the EDX measurement
                            """,
        a_eln={'component': 'NumberEditQuantity'},
    )
    avg_M2 = Quantity(
        type=np.float64,
        description="""
            The average M2 atomic percent from the EDX measurement
                            """,
        a_eln={'component': 'NumberEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUSubstrate` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)
        if self.edx_data_file:
            import pandas as pd

            columns = [
                'Spectrum Label',
                'X (mm)',
                'Y (mm)',
                'Substrate Si Atomic %',
                'Layer 1 Density (g/cm³)',
                'Layer 1 Thickness (nm)',
                'Layer 1 P Atomic %',
                'Layer 1 S Atomic %',
                'Layer 1 Cu Atomic %']

            with archive.m_context.raw_file(self.edx_data_file, 'r') as edx:
                #df_data = pd.read_excel(edx, header=0)
                df_data = pd.read_csv(edx, sep=',', header=0, names=columns )

            self.avg_S = df_data['Layer 1 S Atomic %'].mean()
            self.avg_P = df_data['Layer 1 P Atomic %'].mean()
            self.avg_M1 = df_data['Layer 1 Cu Atomic %'].mean()
            self.avg_M2 = 0
            #Extracting the atomic percent from the EDX file, average and populate




m_package.__init_metainfo__()
