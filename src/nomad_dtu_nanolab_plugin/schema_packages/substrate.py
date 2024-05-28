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
        a_eln={'component': 'StringEditQuantity'},
    )
    substrate_polishing = Quantity(
        type=MEnum(['1 sided', '2 sided', 'none']),
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    doping_type_of_substrate = Quantity(
        type=MEnum(['n', 'p', 'none']),
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    doping_of_substrate = Quantity(
        type=np.float64,
        description="""
            The doping of the substrate measured as the electrical resistivity.
        """,
        a_eln={'component': 'NumberEditQuantity'},
        unit='ohm*cm',
    )
    doping_elements = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    length = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    width = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    thickness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    substrate_history = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
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


m_package.__init_metainfo__()
