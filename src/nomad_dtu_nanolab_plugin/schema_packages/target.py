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
from nomad.datamodel.metainfo.annotations import (
    BrowserAnnotation,
    ELNAnnotation,
    ELNComponentEnum,
)
from nomad.datamodel.metainfo.basesections import CompositeSystem
from nomad.metainfo import Datetime, Package, Quantity, Section

from nomad_dtu_nanolab_plugin.categories import DTUNanolabCategory

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='DTU customised Target scheme')


class DTUTarget(CompositeSystem, Schema):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[DTUNanolabCategory],
        label='Target',
    )
    supplier_id = Quantity(
        type=str,
        default = 'Testbourne',
        a_eln={'component': 'StringEditQuantity'},
    )
    purity = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    impurity_file = Quantity(
        type=str,
        a_browser=BrowserAnnotation(adaptor='RawFileAdaptor'),
        description="""
        Upload a text file specifying the impurities here.
        File has to be created with a seperate code.
        """,
        a_eln={'component': 'FileEditQuantity', 'label': 'file with impurities'},
    )
    impurities = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    thickness = Quantity(
        type=np.float64,
        default = 0.00635,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='m',
    )
    magkeeper_Target = Quantity(
        type=bool,
        default=True,
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )
    target_history = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )
    refill_or_mounting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    time_used = Quantity(
        type=np.float64,
        description='The time the target or cracker has been used in the system',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='s',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUTargets` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)

        if self.impurity_file:
            import pandas as pd

            with archive.m_context.raw_file(self.impurity_file, 'r') as impurity:
                df_data = pd.read_csv(impurity, delimiter='\t', header=0)
                self.impurities = df_data.to_string(index=False)

        number = len(df_data)
        j=0
        for j in range(number):
            self.component[j].name= str(df_data.iloc[0, j]) + ' impurity'
            if df_data.iloc[2, j] =='ppm':
                self.component[j].mass_fraction = df_data.iloc[1,j]/1000000
            elif df_data.iloc[2, j] =='wt%':
                self.component[j].mass_fraction = df_data.iloc[1,j]/100
            elif df_data.iloc[2, j] == 'ppb':
                self.component[j].mass_fraction = df_data.iloc[1,j]/1000000000




m_package.__init_metainfo__()
