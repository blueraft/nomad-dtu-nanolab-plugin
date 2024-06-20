from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_dtu_nanolab_plugin.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)


class SputteringEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_dtu_nanolab_plugin.schema_packages.sputtering import m_package

        return m_package


sputtering = SputteringEntryPoint(
    name='Sputtering',
    description='Schema package defined for sputtering.',
)


class GasEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_dtu_nanolab_plugin.schema_packages.gas import m_package

        return m_package


gas = GasEntryPoint(
    name='Gas',
    description='Schema package defined for gas.',
)


class TargetEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_dtu_nanolab_plugin.schema_packages.target import m_package

        return m_package


target = TargetEntryPoint(
    name='Targets',
    description='Schema package defined for targets.',
)


class SubstrateEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_dtu_nanolab_plugin.schema_packages.substrate import m_package

        return m_package


substrate = SubstrateEntryPoint(
    name='Substrate',
    description='Schema package defined for substrate.',
)


class InstrumentEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_dtu_nanolab_plugin.schema_packages.instrument import m_package

        return m_package


instrument = InstrumentEntryPoint(
    name='Instrument',
    description='Schema package defined for instrument.',
)
