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
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections import CompositeSystemReference
from nomad.metainfo import MEnum, Package, Quantity, Section, SubSection
from nomad_material_processing.vapor_deposition import ChamberEnvironment, GasFlow
from nomad_material_processing.vapor_deposition.pvd import PVDSource, PVDStep
from nomad_material_processing.vapor_deposition.pvd.sputtering import SputterDeposition

from nomad_dtu_nanolab_plugin.categories import DTUNanolabCategory
from nomad_dtu_nanolab_plugin.schema_packages.gas import DTUGasSupply

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='DTU customised sputter Schemas')


class DTUsamples(CompositeSystemReference, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    Substrate_position_x = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    Substrate_position_y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm'},
        unit='m',
    )
    method_of_contact = Quantity(
        type=MEnum(['clamps', 'frame', 'other']),
        default='clamps',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUsamples` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Chamber(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    shutters_open = Quantity(
        type=bool,
        default=False,
        description="""
            Position of the substrate shutter.
        """,
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )
    applied_RF_bias_platen = Quantity(
        type=np.float64,
        default= 0,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    total_pressure = Quantity(
        type=np.float64,
        default= 0.6666,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mtorr'},
        unit='kg/(m*s^2)',
    )


class Substrate(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    set_point_temperature = Quantity(
        type=np.float64,
        default =300,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )
    corrected_real_temperature = Quantity(
        type=np.float64,
        derived = lambda a: a.set_point_temperature*0.905+12,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )


class SCracker(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    Zone1_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )
    Zone2_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )
    Zone3_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )
    valve_ON_time = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 's'},
        unit='s',
    )
    valve_frequency = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'Hz'},
        unit='1/s',
    )
    S_partial_pressure = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='kg/(m*s^2)',
    )


class Special(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    platen_temperature_ramp_rate = Quantity(
        type=np.float64,
        default = 0.3333,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC/minute'},
        unit='kelvin/s',
    )
    target_ramp_rate = Quantity(
        type=np.float64,
        default  =1,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W/second'},
        unit='(kg*m^2)/s^4',
    )
    active_targets = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    active_gases = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    total_deposition_rate = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'angstrom/s'},
        unit='m/s',
    )


class DTUsputter_parameters(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    chamber = SubSection(
        section_def=Chamber,
    )
    substrate = SubSection(
        section_def=Substrate,
    )
    S_cracker = SubSection(
        section_def=SCracker,
    )
    special = SubSection(
        section_def=Special,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUsputter_parameters` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class DTUsource(PVDSource, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    source_shutter_open = Quantity(
        type=bool,
        default=False,
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )

    power_type = Quantity(
        type=MEnum(['RF', 'DC', 'pulsed_DC']),
        default = 'RF',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    applied_voltage = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    applied_power = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='(kg*m^2)/s^3',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUsource` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class DTUGasFlow(GasFlow, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    gas_supply = Quantity(
        type=DTUGasSupply,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUGasFlow` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class DTUChamberEnvironment(ChamberEnvironment, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    gas_flow = SubSection(
        section_def=DTUGasFlow,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUChamberEnvironment` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class DTUsteps(PVDStep, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    sources = SubSection(
        section_def=DTUsource,
        repeats=True,
    )
    sputter_parameters = SubSection(
        section_def=DTUsputter_parameters,
        repeats=True,
    )
    environment = SubSection(
        section_def=DTUChamberEnvironment,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUsteps` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EndOfProcess(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    taken_out = Quantity(
        type=MEnum(['front', 'back']),
        default = 'front',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    Heater_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )
    time_in_chamber_after_ending_deposition = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='s',
    )
    chamber_purged = Quantity(
        type=bool,
        default=False,
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )


class AdjustedInstrumentParameters(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    platen_rotation = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degree'},
        unit='rad',
    )
    stage_used = Quantity(
        type=MEnum(['heating', 'cooling']),
        default = 'heating',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    mask_used = Quantity(
        type=bool,
        default=False,
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )
    mask_description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )


class DepositionParameters(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    deposition_temperature = Quantity(
        type=np.float64,
        default = 300,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'degC'},
        unit='kelvin',
    )
    sputter_pressure = Quantity(
        type=np.float64,
        default = 0.6666,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mtorr'},
        unit='kg/(m*s^2)',
    )
    material_space = Quantity(
        type=str,
        default = '-P-S',
        a_eln={'component': 'StringEditQuantity'},
    )
    applied_power = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='(kg*m^2)/s^3',
    )
    plasma_ignited_at = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='(kg*m^2)/s^3',
    )
    power_type = Quantity(
        type=MEnum(['DC', 'RF', 'pulsed_DC']),
        default = 'RF',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    stable_average_voltage = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    comments_about_voltage = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    Ar_flow = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'cm^3/minute'},
        unit='m^3/s',
    )
    H2S_in_Ar_flow = Quantity(
        type=np.float64,
        description="""
            Flow of 10% H2S in Ar in equivalent flow at standard conditions 0, i.e.
            the equivalent rate at a temperature of 0 °C (273.15 K) and a pressure of
            1 atm (101325 Pa).
        """,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'cm^3/minute',
            'label': 'H2S in Ar flow',
        },
        unit='m^3/s',
    )
    PH3_in_Ar_flow = Quantity(
        type=np.float64,
        description="""
            Flow of 10% PH3 in Ar in equivalent flow at standard conditions 0, i.e.
            the equivalent rate at a temperature of 0 °C (273.15 K) and a pressure of
            1 atm (101325 Pa).
        """,
        a_eln={
            'component': 'NumberEditQuantity',
              'defaultDisplayUnit': 'cm^3/minute',
              'label': 'PH3 in Ar flow',
              },
        unit='m^3/s',
    )
    heating_procedure_description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    cooling_procedure_description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    m_def = Section()
    deposition_time = Quantity(
        type=np.float64,
        default = 1800,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='s',
    )
    boolean_test = Quantity(
        type=bool,
        default=False,
        a_eln=ELNAnnotation(component=ELNComponentEnum.BoolEditQuantity),
    )
    if boolean_test:
        additional_quantity_test = Quantity(
            type=np.float64,
            default = 0.5,
            a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
            unit='(kg*m^2)/s^3',
        )
    else:
        additional_quantity_test = Quantity(
            type=np.float64,
            default = 100,
            a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
            unit='V',
        )


class DTUSputtering(SputterDeposition, Schema):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        categories=[DTUNanolabCategory],
        label='Sputtering',
    )
    lab_id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'Run ID'},
    )
    log_file = Quantity(
        type=str,
        a_eln={'component': 'FileEditQuantity', 'label': 'Log file'},
    )
    samples = SubSection(
        section_def=DTUsamples,
        repeats=True,
    )
    steps = SubSection(
        section_def=DTUsteps,
        repeats=True,
    )
    end_of_process = SubSection(
        section_def=EndOfProcess,
    )
    adjusted_instrument_parameters = SubSection(
        section_def=AdjustedInstrumentParameters,
    )
    deposition_parameters = SubSection(
        section_def=DepositionParameters,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `DTUSputtering` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


m_package.__init_metainfo__()
