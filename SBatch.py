#!/usr/bin/env python 
# catGetDatasetInfo v7-4-4 # to make dataset lists
# sed -i 's/^\/store/root:\/\/cms-xrdr.sdfarm.kr:1094\/\/xrd\/store/g' *

import os, json, array
import numpy as np
from math import ceil       
username = os.environ['USER']

analysis = 'tth2mu'
#analysis = 'TtbarDiLeptonAnalyzer'
pythonCfg = 'tth2mu.py'
#analysis=analysis+'Silver'
RunFiles = [
#              'WMinusH_HToMuMu',
#              'WPlusH_HToMuMu',
#              'ZH_HToMuMu',
#              'VBF_HToMuMu',
#              'GG_HToMuMu',
#              "WWTo2L2Nu",
#              "WZTo3LNu_amcatnlo",
#              "WZTo2L2Q",
#              "ZZTo2L2Nu",
#              "ZZTo2L2Q",
#              "ZZTo4L",
#              "WWW",
#              "WWZ",
#              "WZZ",
#              "ZZZ",
#              "ttZToLLNuNu",
#              "ttWToLNu",
#              "SingleTop_tW_noHadron",
#              "SingleTbar_tW_noHadron",
#              "SingleTop_tW",
#              "SingleTbar_tW",
#              "TTJets_DiLept",
#              "TTJets_DiLept_Tune4",
#              'TTJets_aMC', 
#              'DYJets',
#              'DYJets_MG_10to50',
#              'DYJets_MG2',
#              'DYJets_2J',
#              'DYJets_1J',
#              'DYJets_0J',
#              'DYJets_10to50', 
         #     '2SingleMuon2_Run2016B',
              'SingleMuon2_Run2016C',
         #     'SingleMuon2_Run2016D',
         #     'SingleMuon2_Run2016E',
         #     'SingleMuon2_Run2016F',
         #     'SingleMuon2_Run2016G',
         #     'SingleMuon2_Run2016H',
            #  'SingleMuon_Run2016B',
            #  'SingleMuon_Run2016C',
            #  'SingleMuon_Run2016D',
            #  'SingleMuon_Run2016E',
            #  'SingleMuon_Run2016F',
            #  'SingleMuon_Run2016G',
            #  'SingleMuon_Run2016H_v2',
            #  'SingleMuon_Run2016H_v3',
              ]
datadir = os.environ["CMSSW_BASE"]+'/src/CATTools/CatAnalyzer/test/Nano_AOD/Data/'
#version = os.environ["CMSSW_VERSION"]



for i in RunFiles:
    datasetName = i
    fileList = datadir + datasetName + '.txt'
    files = np.array([])
    for f in open(fileList).readlines():
        f = f.strip()
        f = f.strip('\',"')
        if len(f) < 5: continue
        if '#' == f[0] or '.root' != f[-5:]: continue
        files = np.append(files,[f])
    nFiles = len(files)     
    maxFiles = 20
    nSection = int(ceil(1.0*nFiles/maxFiles))
    for section in range(nSection):
        begin = section*maxFiles
        end = min(begin + maxFiles, nFiles)
        FileNames = files[begin:end]
        FileNamesStr = " ".join(str(i) for i in FileNames)
        print FileNamesStr
        #jobName = analysis+'_'+datasetName
        #createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 10"%(pythonCfg, jobName, fileList) 
        subBatch = "condor_submit tth2mu_cfg.jds -append arguments=%s" %(FileNamesStr)
        #createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 20 --transferDest \"root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/%s/NanoAOD/%s/%s\""%(pythonCfg, jobName, fileList, username, version, datasetName)
        #print createbatch
        print subBatch 
            
        os.system(subBatch)
