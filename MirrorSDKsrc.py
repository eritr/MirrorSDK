# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: E:/Documents/maya/2018/scripts\MirrorSDK.py
# Compiled at: 2018-06-18 08:42:33

# Длязапускаиспользовать
# import MirrorSDKExtended
# MirrorSDK.MirrorSDKUIExtended()


import pymel.core as pm
import maya.cmds as mc
import sys


def MirrorSDKUIExtended():
    TitleWindow = 'MirrorSDK (Extended by Aleksei S.)'
    if pm.window(TitleWindow, q=True, ex=True):
        pm.deleteUI(TitleWindow)
    pm.window(TitleWindow)
    pm.showWindow()
    pm.columnLayout(adj=True)
    pm.separator(st=None, h=10)
    pm.text(l=TitleWindow, bgc=(0.1, 0.5, 0.5))
    pm.textFieldGrp('search', l='Search:', tx='_L')
    pm.radioButtonGrp('selt', nrb=2, l='Type:', la2=(
        'Translate', 'BlendShape (not work)'), sl=1, en2=False, cc='changeUI')
    pm.checkBoxGrp('checkbox2', ncb=3, l='TranslateAix:', la3=('X', 'Y', 'Z'))
    pm.checkBoxGrp('checkbox3', ncb=3, l='RotateAix:', la3=('X', 'Y', 'Z'))
    pm.checkBoxGrp('checkbox4', ncb=3, l='ScaleAix:', la3=('X', 'Y', 'Z'))
    pm.textFieldButtonGrp('getCtrl1', l='FirstCtrl:',
                          tx='', bl='Get', bc=getCtrl1c)
    pm.textFieldButtonGrp('getCtrl2', l='SecondCtrl:', bl='Get', bc=getCtrl2c)
    pm.textFieldButtonGrp(
        'getAttribute1', l='ControlAttribute:', bl='Get', bc=getAttribute1c)
    pm.textFieldButtonGrp('getCtrlgrp1', l='DrivenObj:',
                          bl='Get', bc=getCtrlgrp1c)
    pm.floatFieldGrp('getfloat', nf=2, l='ControlValue', v1=0, v2=90)
    pm.separator(st=None, h=10)
    pm.button('button1', l='After the information is confirmed, click the execution step 1, then adjust the object being driven.', c=SDK1, bgc=(0.0,
                                                                                                                                                0.3,
                                                                                                                                                0.1))
    pm.separator(st=None, h=10)
    pm.button('button2', l='Finish step1, click This completes the mirror or non mirror operation', c=SDK2, bgc=(0,
                                                                                                                 0.4,
                                                                                                                 0.1))
    return


def getCtrl1c():
    getCtrl1c_list = pm.ls(sl=True)
    if len(getCtrl1c_list) > 1:
        pm.error('Only one object can be selected')
    pm.textFieldButtonGrp('getCtrl1', e=True, tx=getCtrl1c_list[0])


def getCtrl2c():
    getCtrl2c_list = pm.ls(sl=True)
    if len(getCtrl2c_list) > 1:
        pm.error('Only one object can be selected')
    pm.textFieldButtonGrp('getCtrl2', e=True, tx=getCtrl2c_list[0])


def getAttribute1c():
    mainChannelBox = pm.channelBox('mainChannelBox', q=True, sma=True)
    if len(mainChannelBox) > 1:
        pm.error('Only one attribute can be selected')
    pm.textFieldButtonGrp('getAttribute1', e=True, tx=mainChannelBox[0])


def getCtrlgrp1c():
    # Вот ради списка выделенных элементов тут подгружена библиотека майки? Ужас.
    pm.textFieldButtonGrp('getCtrlgrp1', e=True, tx=(',').join(mc.ls(sl=True)))


def SDK1(*O0OOOOO00O000O0O0):
    txtField_getCtrl1_list = pm.textFieldButtonGrp('getCtrl1', q=True, tx=True)
    txtField_getCtrl2_list = pm.textFieldButtonGrp('getCtrl2', q=True, tx=True)
    txtField_getCtrlGrp1_list = pm.textFieldButtonGrp(
        'getCtrlgrp1', q=True, tx=True)
    exDrivenElems = txtField_getCtrlGrp1_list.split(',')
    exControlAttribute = pm.textFieldButtonGrp(
        'getAttribute1', q=True, tx=True)
    exMinValue = pm.floatFieldGrp('getfloat', q=True, v1=True)
    exMaxValue = pm.floatFieldGrp('getfloat', q=True, v2=True)
    exFirstCtrl = pm.textFieldButtonGrp('getCtrl1', q=True, tx=True)
    exListCtrlAttributes = ['tx', 'ty', 'tz',
                            'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    pm.setAttr(txtField_getCtrl1_list + '.' +
               exControlAttribute, exMinValue)
    for exDrivenElem in exDrivenElems:
        for exCtrlAttrElem in exListCtrlAttributes:
            pm.setDrivenKeyframe(exDrivenElem + '.' + exCtrlAttrElem,
                                 cd=txtField_getCtrl2_list + '.' + exControlAttribute)

    pm.setAttr(txtField_getCtrl1_list + '.' +
               exControlAttribute, exMaxValue)


def SDK2(*OO000OOO000OO0000):
    O000O000O0O0OOOO0 = pm.textFieldButtonGrp('getCtrl1', q=True, tx=True)
    OOO000O00OOOOO00O = pm.textFieldButtonGrp('getCtrl2', q=True, tx=True)
    O000O0OOO0O0OO00O = pm.textFieldButtonGrp('getCtrlgrp1', q=True, tx=True)
    OOOO0OO000OOOO0O0 = O000O0OOO0O0OO00O.split(',')
    OOO000O0O000000OO = pm.textFieldButtonGrp('getAttribute1', q=True, tx=True)
    O00000O00OOOOO000 = pm.floatFieldGrp('getfloat', q=True, v1=True)
    OOO000O000O0000OO = pm.floatFieldGrp('getfloat', q=True, v2=True)
    OO0OO0O00O0OO00O0 = pm.textFieldButtonGrp('getCtrl1', q=True, tx=True)
    O000OO000000O0000 = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    O0O0OOOOO0O0O0OOO = pm.textFieldGrp('search', q=True, tx=True)
    O0OO000O0OOOOOO0O = O0O0OOOOO0O0O0OOO.replace('L', 'R') if ('_L_').find(
        O0O0OOOOO0O0O0OOO) >= 0 else O0O0OOOOO0O0O0OOO.replace('R', 'L')
    OOO00O0OOO0O000OO = O000O000O0O0OOOO0.replace(O0O0OOOOO0O0O0OOO, O0OO000O0OOOOOO0O) if O000O000O0O0OOOO0.find(
        O0O0OOOOO0O0O0OOO) >= 0 else O000O000O0O0OOOO0.replace(O0OO000O0OOOOOO0O, O0O0OOOOO0O0O0OOO)
    O0OO00OOO0OOO0000 = OOO000O00OOOOO00O.replace(O0O0OOOOO0O0O0OOO, O0OO000O0OOOOOO0O) if O000O000O0O0OOOO0.find(
        O0O0OOOOO0O0O0OOO) >= 0 else OOO000O00OOOOO00O.replace(O0OO000O0OOOOOO0O, O0O0OOOOO0O0O0OOO)
    O0O0O00OOOOOO00O0 = OOO000O0O000000OO.replace(O0O0OOOOO0O0O0OOO, O0OO000O0OOOOOO0O) if O000O000O0O0OOOO0.find(
        O0O0OOOOO0O0O0OOO) >= 0 else OOO000O0O000000OO.replace(O0OO000O0OOOOOO0O, O0O0OOOOO0O0O0OOO)
    if pm.objExists(OOO00O0OOO0O000OO):
        O00O0O0OOO0000OO0 = - \
            1 if pm.checkBoxGrp('checkbox2', q=True, v1=True) else 1
        O00O0OOOOOOO0OOO0 = - \
            1 if pm.checkBoxGrp('checkbox2', q=True, v2=True) else 1
        O0O0000O00OO0OOO0 = - \
            1 if pm.checkBoxGrp('checkbox2', q=True, v3=True) else 1
        OO000O0O0O00OOOOO = - \
            1 if pm.checkBoxGrp('checkbox3', q=True, v1=True) else 1
        O000OO0OOOO0OO0O0 = - \
            1 if pm.checkBoxGrp('checkbox3', q=True, v2=True) else 1
        O000OO0000OOOOOOO = - \
            1 if pm.checkBoxGrp('checkbox3', q=True, v3=True) else 1
        pm.setAttr(OOO00O0OOO0O000OO + '.' +
                   O0O0O00OOOOOO00O0, O00000O00OOOOO000)
        for O000O0O0O00O0O0OO in OOOO0OO000OOOO0O0:
            O00OO0000OO00OOO0 = O000O0O0O00O0O0OO.replace(O0O0OOOOO0O0O0OOO, O0OO000O0OOOOOO0O) if O000O000O0O0OOOO0.find(
                O0O0OOOOO0O0O0OOO) >= 0 else O000O0O0O00O0O0OO.replace(O0OO000O0OOOOOO0O, O0O0OOOOO0O0O0OOO)
            for O00O0O000OO000O00 in O000OO000000O0000:
                pm.setDrivenKeyframe(O00OO0000OO00OOO0 + '.' + O00O0O000OO000O00,
                                     cd=O0OO00OOO0OOO0000 + '.' + O0O0O00OOOOOO00O0)

        pm.setAttr(OOO00O0OOO0O000OO + '.' +
                   O0O0O00OOOOOO00O0, OOO000O000O0000OO)
        for O000O0O0O00O0O0OO in OOOO0OO000OOOO0O0:
            O00OO0000OO00OOO0 = O000O0O0O00O0O0OO.replace(O0O0OOOOO0O0O0OOO, O0OO000O0OOOOOO0O) if O000O000O0O0OOOO0.find(
                O0O0OOOOO0O0O0OOO) >= 0 else O000O0O0O00O0O0OO.replace(O0OO000O0OOOOOO0O, O0O0OOOOO0O0O0OOO)
            OOO0OOO0OO0O00000 = pm.getAttr(O000O0O0O00O0O0OO + '.translate')
            OOO0OOO0OOOO0OOO0 = pm.getAttr(O000O0O0O00O0O0OO + '.rotate')
            pm.setAttr(O00OO0000OO00OOO0 + '.translate', (O00O0O0OOO0000OO0 *
                       OOO0OOO0OO0O00000[0], O00O0OOOOOOO0OOO0 * OOO0OOO0OO0O00000[1], O0O0000O00OO0OOO0 * OOO0OOO0OO0O00000[2]))
            pm.setAttr(O00OO0000OO00OOO0 + '.rotate', (OO000O0O0O00OOOOO *
                       OOO0OOO0OOOO0OOO0[0], O000OO0OOOO0OO0O0 * OOO0OOO0OOOO0OOO0[1], O000OO0000OOOOOOO * OOO0OOO0OOOO0OOO0[2]))

        for O000O0O0O00O0O0OO in OOOO0OO000OOOO0O0:
            O00OO0000OO00OOO0 = O000O0O0O00O0O0OO.replace(O0O0OOOOO0O0O0OOO, O0OO000O0OOOOOO0O) if O000O000O0O0OOOO0.find(
                O0O0OOOOO0O0O0OOO) >= 0 else O000O0O0O00O0O0OO.replace(O0OO000O0OOOOOO0O, O0O0OOOOO0O0O0OOO)
            for O00O0O000OO000O00 in O000OO000000O0000:
                pm.setDrivenKeyframe(O00OO0000OO00OOO0 + '.' + O00O0O000OO000O00,
                                     cd=O0OO00OOO0OOO0000 + '.' + O0O0O00OOOOOO00O0)

        print 'Mirror SDK completion!!!',
    else:
        for O000O0O0O00O0O0OO in OOOO0OO000OOOO0O0:
            for O00O0O000OO000O00 in O000OO000000O0000:
                pm.setDrivenKeyframe(O000O0O0O00O0O0OO + '.' + O00O0O000OO000O00,
                                     cd=OOO000O00OOOOO00O + '.' + OOO000O0O000000OO)

        print 'Non mirror drive completion!!!',
