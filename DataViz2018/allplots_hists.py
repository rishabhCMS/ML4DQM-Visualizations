#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:20:04 2019

@author: rishabh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time

def plots(x, quantile, title):
    
    fig = plt.figure()
    plt.xlabel("{}".format(quantile))
    plt.ylabel("Quantile_Value")
    plt.title(title)
    #plt.text(0.9, 0.9, r'$\mu=100,\ \sigma=15$')
    plt.hist(x, density=True, facecolor='g', alpha=0.75)
    plt.grid(True)
    # plt.show()
    fig.savefig('{}.png'.format(title))
    del fig
if __name__ == "__main__":
    
    '''feature declaration as per the twiki'''
    start = time.time()
    features_new_egamma = ["qpVtxChi2",
                    "qpVtxNtr",
                    "qPUEvt",
                    "qlumiEvt",
                    "qGsfPt",
                    "qGsfEta",
                    "qGsfPhi",
                    "qGsfN",
                    "qPhoN",
                    "gedPhoPt",
                    "gedPhoEta",
                    "gedPhoPhi",
                    "gedPhoEn",
                    "gedPhoe3x3",
                    "qSigmaIEta",
                    "qSigmaIPhi"]

    features_new_singlemuon = ["qPUEvt",
                           "qlumiEvt",
                           "qMuN",
                           "qMuNCh",
                           "qMuPt",
                           "qMuEta",
                           "qMuPhi",
                           "qMuEn",
                           "qMuChi2"]

    features_new_jetht_1 = ["qpVtxChi2",
                      "qpVtxNtr",
                      "qPUEvt",
                      "qlumiEvt",
                      "qPFJetN",
                      "qPFJetPt",
                      "qPFJetPhi",
                      "qPFJetEta",
                      "qPFMetPt",
                      "qPFMetPhi",
                      "qCalJetN",
                      "qCalJetPt",
                      "qCalJetEta",
                      "qCalJetPhi",
                      "qCalJetEn",
                      "qCalMETPt",
                      "qCalMETPhi",]
    features_new_jetht_2 = ["qCCEn",
                      "qCCEta",
                      "qCCPhi",
                      "qSCEn",
                      "qSCEta",
                      "qSCPhi"]

    features_new_zerobias = ["qpVtxChi2",
                     "qpVtxNtr",
                     "qPUEvt",
                     "qlumiEvt",
                     "qgTkPt",
                     "qgTkEta",
                     "qgTkPhi",
                     "qgTkN",
                     "qgTkChi2",
                     "qgTkNHits",
                     "qgTkNLay"]
    
    '''data location'''
    PD_GOOD_DATA_DIRECTORY = "/afs/cern.ch/work/p/ppayoung/public/data2018/prompt_reco_2018/good_data/"
    PD_BAD_DATA_DIRECTORY = "/afs/cern.ch/work/p/ppayoung/public/data2018/prompt_reco_2018/bad_data/"
    PD_DCS_BAD_DATA_DIRECTORY = "/afs/cern.ch/work/p/ppayoung/public/data2018/prompt_reco_2018/dcs_bad_data/"
    #PD_FAILURE_DATA_DIRECTORY = "/afs/cern.ch/work/p/ppayoung/public/data2018/prompt_reco_2018/failures/"
    
    
    
    '''creating dataframes'''
    
    
    df_EGamma     = pd.read_csv(os.path.join(PD_GOOD_DATA_DIRECTORY,"EGamma_feature2.csv"))
    df_ZeroBias   = pd.read_csv(os.path.join(PD_GOOD_DATA_DIRECTORY,"ZeroBias_feature2.csv"))
    df_JetHT      = pd.read_csv(os.path.join(PD_GOOD_DATA_DIRECTORY,"JetHT_feature2.csv"))
    df_SingleMuon = pd.read_csv(os.path.join(PD_GOOD_DATA_DIRECTORY,"SingleMuon_feature2.csv"))
    

    
    '''removing unwanted features from dataframes'''
    
    cols_egamma = []
    for feature in features_new_egamma:
        a = [col for col in df_EGamma.columns if "{}".format(feature) in col] 
        cols_egamma = cols_egamma + a
    new_cols_egamma = []
    new_cols_egamma = cols_egamma + ["lumiId", "lumi", "EventsPerLs", "runId"]
    
    cols_zerobias = []
    for feature in features_new_zerobias:
        a = [col for col in df_ZeroBias.columns if "{}".format(feature) in col] 
        cols_zerobias = cols_zerobias + a
    new_cols_zerobias = []
    new_cols_zerobias = cols_zerobias + ["lumiId", "lumi", "EventsPerLs", "runId"]
    
    cols_jetht_1 = []
    for feature in features_new_jetht_1:
        a = [col for col in df_JetHT.columns if "{}".format(feature) in col] 
        cols_jetht_1 = cols_jetht_1 + a
    new_cols_jetht_1 = []
    new_cols_jetht_1 = cols_jetht_1 + ["lumiId", "lumi", "EventsPerLs", "runId"]

    cols_jetht_2 = []
    for feature in features_new_jetht_2:
        a = [col for col in df_JetHT.columns if "{}".format(feature) in col] 
        cols_jetht_2 = cols_jetht_2 + a
    new_cols_jetht_2 = []
    new_cols_jetht_2 = cols_jetht_2 + ["lumiId", "lumi", "EventsPerLs", "runId"]
    
    cols_singlemuon = []
    for feature in features_new_egamma:
        a = [col for col in df_SingleMuon.columns if "{}".format(feature) in col] 
        cols_singlemuon = cols_singlemuon + a
    new_cols_singlemuon = []
    new_cols_singlemuon = cols_singlemuon + ["lumiId", "lumi", "EventsPerLs", "runId"]
    

    '''new DFs with new cols'''

    df_EGamma_new = df_EGamma[new_cols_egamma]
    df_finite_EGamma = df_EGamma_new.fillna(0)
    df_finite_EGamma_limit = df_finite_EGamma[df_finite_EGamma["EventsPerLs"] > 500]
    
    df_ZeroBias_new = df_ZeroBias[new_cols_zerobias]
    df_finite_ZeroBias = df_ZeroBias_new.fillna(0)
    df_finite_ZeroBias_limit = df_finite_ZeroBias[df_finite_ZeroBias["EventsPerLs"] > 500]
    
    df_JetHT_new_1 = df_JetHT[new_cols_jetht_1]
    df_finite_JetHT_1 = df_JetHT_new_1.fillna(0)
    df_finite_JetHT_limit_1 = df_finite_JetHT_1[df_finite_JetHT_1["EventsPerLs"] > 500]
    
    df_JetHT_new_2 = df_JetHT[new_cols_jetht_2]
    df_finite_JetHT_2 = df_JetHT_new_2.fillna(0)
    df_finite_JetHT_limit_2 = df_finite_JetHT_2[df_finite_JetHT_2["EventsPerLs"] > 500]
    
    df_SingleMuon_new = df_SingleMuon[new_cols_singlemuon]
    df_finite_SingleMuon = df_SingleMuon_new.fillna(0)
    df_finite_SingleMuon_limit = df_finite_SingleMuon[df_finite_SingleMuon["EventsPerLs"] > 500]
    
    '''finding unique run numbers'''
    run_numbers_egamma = df_finite_EGamma_limit["runId"].unique().tolist()
    run_numbers_zerobias = df_finite_ZeroBias_limit["runId"].unique().tolist()
    run_numbers_singlemuon = df_finite_SingleMuon_limit["runId"].unique().tolist()
    run_numbers_jetht_1 = df_finite_JetHT_limit_1["runId"].unique().tolist()
    run_numbers_jetht_2 = df_finite_JetHT_limit_2["runId"].unique().tolist()
    
    '''plotting the hists'''
    
    os.mkdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/egamma/")
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/egamma/")
    for run_number in run_numbers_egamma:
        df_test = df_finite_EGamma_limit[df_finite_EGamma_limit["runId"] == run_number]
        for quantile in cols_egamma:
            plots(df_test[quantile],"{}".format(quantile) ,"{}_{}_eg".format(run_number,quantile))
    
    #source = "/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/bad_dcs_histograms/egamma/"
    #destination = "/eos/user/r/runiyal/ML4DQM_Histograms/bad_dcs_histograms/egamma/"
    #for file_ in os.listdir(source):
        #shutil.move(os.path.join(source,file_), destination)
    #print("the egamma histograms have been moved to {}".format(destination)) 
    
    
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/")
    os.mkdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/jetht_1/")
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/jetht_1/")        
    for run_number in run_numbers_jetht_1:
        df_test = df_finite_JetHT_limit_1[df_finite_JetHT_limit_1["runId"] == run_number]
        for quantile in cols_jetht_1:
            plots(df_test[quantile],"{}".format(quantile) ,"{}_{}_jtht".format(run_number,quantile))

    os.mkdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/jetht_2/")
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/jetht_2/")        
    for run_number in run_numbers_jetht_2:
        df_test = df_finite_JetHT_limit_2[df_finite_JetHT_limit_2["runId"] == run_number]
        for quantile in cols_jetht_2:
            plots(df_test[quantile],"{}".format(quantile) ,"{}_{}_jtht".format(run_number,quantile))
    

    
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/")
    os.mkdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/zerobias/")
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/zerobias/")
        
    for run_number in run_numbers_zerobias:
        df_test = df_finite_ZeroBias_limit[df_finite_ZeroBias_limit["runId"] == run_number]
        for quantile in cols_zerobias:
            plots(df_test[quantile],"{}".format(quantile) ,"{}_{}_zb".format(run_number,quantile))


    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/")
    os.mkdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/singlemuon/")
    os.chdir("/afs/cern.ch/work/r/runiyal/ML4DQM/CMS_DC_ANOMALY/dataViz2018/good_data_histograms/singlemuon/")
    for run_number in run_numbers_singlemuon:
        df_test = df_finite_SingleMuon_limit[df_finite_SingleMuon_limit["runId"] == run_number]
        for quantile in cols_singlemuon:
            plots(df_test[quantile],"{}".format(quantile) ,"{}_{}_sm".format(run_number,quantile))
    print("time taken for this to complete :", time.time()-start," seconds")
