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
from nomad.datamodel.data import ArchiveSection, Schema
from nomad.datamodel.metainfo.basesections import Instrument
from nomad.metainfo import Datetime, Package, Quantity, Section, SubSection

from nomad_dtu_nanolab_plugin.categories import DTUNanolabCategory

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='DTU customised Instrument scheme')


class Purge(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_last_purge = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    number_of_purge_cycles = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    time_per_purge_cycles = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minutes'},
        unit='s',
    )
    pressure_during_purge = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='kg/(m*s^2)',
    )


class ProperCleaning(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_last_cleaning = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    comment_about_last_cleaning = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )


class OpeningToAir(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_last_opened_from_back = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    comment_about_last_opened_to_air = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )


class NonToxicGasInlet(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    non_toxic_gas_inlet_position_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    non_toxic_gas_inlet_position_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    non_toxic_gas_inlet_position_z = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    non_toxic_gas_inlet_direction = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    non_toxic_gas_inlet_pipe_diameter = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='m',
    )


class ToxicGasInlet(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    toxic_gas_inlet_position_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    toxic_gas_inlet_position_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    toxic_gas_inlet_position_z = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    toxic_gas_inlet_direction = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    toxic_gas_inlet_pipe_diameter = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='m',
    )


class TaurusSource(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_changes = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    pointed_towards_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    pointed_towards_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    distance_to_substrate = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    set_angle = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )
    rotation = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )


class Magkeeper3Source(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_changes = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    pointed_towards_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    pointed_towards_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    distance_to_substrate = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    set_angle = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )
    rotation = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )


class Magkeeper4Source(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_changes = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    pointed_towards_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    pointed_towards_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    distance_to_substrate = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    set_angle = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )
    rotation = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )


class SCrackerSource(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    date_of_changes = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    pointed_towards_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    pointed_towards_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    distance_to_substrate = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    set_angle = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degrees'},
        unit='rad',
    )
    S_cracker_extension_into_chamber = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )


class DTUInstrument(Instrument, Schema):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[DTUNanolabCategory],
        label='Instrument',
    )
    time_used_chamber = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minutes'},
        unit='s',
    )
    base_pressure = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='kg/(m*s^2)',
    )
    chamber_history = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    purge = SubSection(
        section_def=Purge,
        repeats=True,
    )
    proper_cleaning = SubSection(
        section_def=ProperCleaning,
        repeats=True,
    )
    opening_to_air = SubSection(
        section_def=OpeningToAir,
        repeats=True,
    )
    non_toxic_gas_inlet = SubSection(
        section_def=NonToxicGasInlet,
        repeats=True,
    )
    toxic_gas_inlet = SubSection(
        section_def=ToxicGasInlet,
        repeats=True,
    )
    Taurus_source = SubSection(
        section_def=TaurusSource,
        repeats=True,
    )
    Magkeeper3_source = SubSection(
        section_def=Magkeeper3Source,
        repeats=True,
    )
    Magkeeper4_source = SubSection(
        section_def=Magkeeper4Source,
        repeats=True,
    )
    S_cracker_source = SubSection(
        section_def=SCrackerSource,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUInstrument` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


m_package.__init_metainfo__()
