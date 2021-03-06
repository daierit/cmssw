import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")
process.load('Configuration.Geometry.GeometryExtended2023D3_cff')
process.load('Configuration.Geometry.GeometryExtended2023D3Reco_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageLogger.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    categories = cms.untracked.vstring('GEMGeometryBuilderFromDDD'),
                                    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
            ),
        GEMGeometryBuilderFromDDD = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
            )
        )
                                    )

process.test = cms.EDAnalyzer("GEMGeometryAnalyzer")

process.p = cms.Path(process.test)

