#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:20:04 2019

@author: rishabh
"""

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import os

def plots(x, y, title):
    
    plt.figure()
    plt.xlabel("Lumi_Id")
    plt.ylabel("Quantile_Value")
    plt.title(title)
    plt.bar(x,y)
    plt.savefig('{}.png'.format(title))
    
if __name__ == "__main__":
    
    '''feature declaration as per the twiki'''
    
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

    features_new_jetht = ["qpVtxChi2",
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
                      "qCalMETPhi",
                      "qCCEn",
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
    
    cols_jetht = []
    for feature in features_new_jetht:
        a = [col for col in df_JetHT.columns if "{}".format(feature) in col] 
        cols_jetht = cols_jetht + a
    new_cols_jetht = []
    new_cols_jetht = cols_jetht + ["lumiId", "lumi", "EventsPerLs", "runId"]
    
    cols_singlemuon = []
    for feature in features_new_egamma:
        a = [col for col in df_SingleMuon.columns if "{}".format(feature) in col] 
        cols_singlemuon = cols_singlemuon + a
    new_cols_singlemuon = []
    new_cols_singlemuon = cols_singlemuon + ["lumiId", "lumi", "EventsPerLs", "runId"]
    

    '''new DFs with new cols'''

    df_EGamma_new = df_EGamma[new_cols_egamma]
    df_ZeroBias_new = df_ZeroBias[new_cols_zerobias]
    df_JetHT_new = df_JetHT[new_cols_jetht]
    df_SingleMuon_new = df_SingleMuon[new_cols_singlemuon]
    
    
    '''finding unique run numbers'''
    run_numbers_egamma = df_EGamma_new["runId"].unique().tolist()
    run_numbers_zerobias = df_ZeroBias_new["runId"].unique().tolist()
    run_numbers_singlemuon = df_SingleMuon_new["runId"].unique().tolist()
    run_numbers_jetht = df_JetHT_new["runId"].unique().tolist()
    
    
    '''plotting the hists'''
    for run_number in run_numbers_egamma:
        df_test = df_EGamma_new[df_EGamma_new["runId"] == run_number]
        for quantile in cols_egamma:
            plots(df_test["lumiId"],df_test[quantile], "{}_{}_egamma".format(run_number,quantile))
            
    for run_number in run_numbers_jetht:
        df_test = df_JetHT_new[df_JetHT_new["runId"] == run_number]
        for quantile in cols_jetht:
            plots(df_test["lumiId"],df_test[quantile], "{}_{}_jetht".format(run_number,quantile))
        
    for run_number in run_numbers_zerobias:
        df_test = df_ZeroBias_new[df_ZeroBias_new["runId"] == run_number]
        for quantile in cols_zerobias:
            plots(df_test["lumiId"],df_test[quantile], "{}_{}_zerobias".format(run_number,quantile))
            
    for run_number in run_numbers_singlemuon:
        df_test = df_SingleMuon_new[df_SingleMuon_new["runId"] == run_number]
        for quantile in cols_singlemuon:
            plots(df_test["lumiId"],df_test[quantile], "{}_{}_singlemuon".format(run_number,quantile))
        
        
        
        
        
        
        
        
        
        
        
