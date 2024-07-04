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
from nomad.metainfo import Datetime, Package, Quantity, Section

from nomad_dtu_nanolab_plugin.categories import DTUNanolabCategory

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='DTU customised gas scheme')


class DTUGasSupply(CompositeSystem, Schema):
    """
    Class autogenerated from yaml schema.
    """
    m_def = Section(
        categories=[DTUNanolabCategory],
        label='Gas Supply',
    )
    molecular_formula = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    molecular_mass = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit' : 'Da'},
        unit='g',
    )
    cas_number = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    supplier_id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    purity = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    impurities = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    date_of_production = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    date_of_installation = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    total_volume_consumption = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'liter'},
        unit='m^3',
    )
    time_used_gas = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minutes'},
        unit='s',
    )
    gas_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    iupac_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    inchi = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    inchi_key = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    smiles = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    canonical_smiles = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )


    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUGasSupply` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


m_package.__init_metainfo__()
