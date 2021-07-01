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
    exListDrivenElems = txtField_getCtrlGrp1_list.split(',')
    exControlAttribute = pm.textFieldButtonGrp(
        'getAttribute1', q=True, tx=True)
    exMinValue = pm.floatFieldGrp('getfloat', q=True, v1=True)
    exMaxValue = pm.floatFieldGrp('getfloat', q=True, v2=True)
    exFirstCtrl = pm.textFieldButtonGrp('getCtrl1', q=True, tx=True)
    exListAllAttributes = ['tx', 'ty', 'tz',
                           'rx', 'ry', 'rz', 'sx', 'sy', 'sz']

    pm.setAttr(txtField_getCtrl1_list + '.' +
               exControlAttribute, exMinValue)

    for exDrivenElem in exListDrivenElems:
        for exAttrElemFromListAllAttributes in exListAllAttributes:
            pm.setDrivenKeyframe(exDrivenElem + '.' + exAttrElemFromListAllAttributes,
                                 cd=txtField_getCtrl2_list + '.' + exControlAttribute)

    pm.setAttr(txtField_getCtrl1_list + '.' +
               exControlAttribute, exMaxValue)


def SDK2(*OO000OOO000OO0000):
    txtField_getCtrl1_list = pm.textFieldButtonGrp('getCtrl1', q=True, tx=True)
    txtField_getCtrl2_list = pm.textFieldButtonGrp('getCtrl2', q=True, tx=True)
    txtField_getCtrlGrp1_list = pm.textFieldButtonGrp(
        'getCtrlgrp1', q=True, tx=True)
    txtField_getCtrlGrp1_list = txtField_getCtrlGrp1_list.split(',')
    exControlAttribute = pm.textFieldButtonGrp(
        'getAttribute1', q=True, tx=True)
    exMinValue = pm.floatFieldGrp('getfloat', q=True, v1=True)
    exMaxValue = pm.floatFieldGrp('getfloat', q=True, v2=True)
    exListAllAttributes = ['tx', 'ty', 'tz',
                           'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    exSearch = pm.textFieldGrp('search', q=True, tx=True)
    exRenamer = exSearch.replace('L', 'R') if ('_L_').find(
        exSearch) >= 0 else exSearch.replace('R', 'L')
    exNewNameCtrl1 = txtField_getCtrl1_list.replace(exSearch, exRenamer) if txtField_getCtrl1_list.find(
        exSearch) >= 0 else txtField_getCtrl1_list.replace(exRenamer, exSearch)
    exNewNameCtrl2 = txtField_getCtrl2_list.replace(exSearch, exRenamer) if txtField_getCtrl1_list.find(
        exSearch) >= 0 else txtField_getCtrl2_list.replace(exRenamer, exSearch)
    exControlAttributeReplaced = exControlAttribute.replace(exSearch, exRenamer) if txtField_getCtrl1_list.find(
        exSearch) >= 0 else exControlAttribute.replace(exRenamer, exSearch)
    if pm.objExists(exNewNameCtrl1):
        extx = - \
            1 if pm.checkBoxGrp('checkbox2', q=True, v1=True) else 1
        exty = - \
            1 if pm.checkBoxGrp('checkbox2', q=True, v2=True) else 1
        extz = - \
            1 if pm.checkBoxGrp('checkbox2', q=True, v3=True) else 1
        exrx = - \
            1 if pm.checkBoxGrp('checkbox3', q=True, v1=True) else 1
        exry = - \
            1 if pm.checkBoxGrp('checkbox3', q=True, v2=True) else 1
        exrz = - \
            1 if pm.checkBoxGrp('checkbox3', q=True, v3=True) else 1
        exsx = - \
            1 if pm.checkBoxGrp('checkbox4', q=True, v3=True) else 1
        exsy = - \
            1 if pm.checkBoxGrp('checkbox4', q=True, v3=True) else 1
        exsz = - \
            1 if pm.checkBoxGrp('checkbox4', q=True, v3=True) else 1
        pm.setAttr(exNewNameCtrl1 + '.' +
                   exControlAttributeReplaced, exMinValue)
        for exCtrlElemFromGrp1 in txtField_getCtrlGrp1_list:
            exMirroredCtrl = exCtrlElemFromGrp1.replace(exSearch, exRenamer) if txtField_getCtrl1_list.find(
                exSearch) >= 0 else exCtrlElemFromGrp1.replace(exRenamer, exSearch)
            for ExElemFromListAllAttributes in exListAllAttributes:
                pm.setDrivenKeyframe(exMirroredCtrl + '.' + ExElemFromListAllAttributes,
                                     cd=exNewNameCtrl2 + '.' + exControlAttributeReplaced)

        pm.setAttr(exNewNameCtrl1 + '.' +
                   exControlAttributeReplaced, exMaxValue)
        for exCtrlElemFromGrp1 in txtField_getCtrlGrp1_list:
            exMirroredCtrl = exCtrlElemFromGrp1.replace(exSearch, exRenamer) if txtField_getCtrl1_list.find(
                exSearch) >= 0 else exCtrlElemFromGrp1.replace(exRenamer, exSearch)
            exMirroredCtrlTranslate = pm.getAttr(
                exCtrlElemFromGrp1 + '.translate')
            exMirroredCtrlRotate = pm.getAttr(exCtrlElemFromGrp1 + '.rotate')
            pm.setAttr(exMirroredCtrl + '.translate', (extx *
                       exMirroredCtrlTranslate[0], exty * exMirroredCtrlTranslate[1], extz * exMirroredCtrlTranslate[2]))
            pm.setAttr(exMirroredCtrl + '.rotate', (exrx *
                       exMirroredCtrlRotate[0], exry * exMirroredCtrlRotate[1], exrz * exMirroredCtrlRotate[2]))

        for exCtrlElemFromGrp1 in txtField_getCtrlGrp1_list:
            exMirroredCtrl = exCtrlElemFromGrp1.replace(exSearch, exRenamer) if txtField_getCtrl1_list.find(
                exSearch) >= 0 else exCtrlElemFromGrp1.replace(exRenamer, exSearch)
            for ExElemFromListAllAttributes in exListAllAttributes:
                pm.setDrivenKeyframe(exMirroredCtrl + '.' + ExElemFromListAllAttributes,
                                     cd=exNewNameCtrl2 + '.' + exControlAttributeReplaced)

        print 'Mirror SDK completion!!!',
    else:
        for exCtrlElemFromGrp1 in txtField_getCtrlGrp1_list:
            for ExElemFromListAllAttributes in exListAllAttributes:
                pm.setDrivenKeyframe(exCtrlElemFromGrp1 + '.' + ExElemFromListAllAttributes,
                                     cd=txtField_getCtrl2_list + '.' + exControlAttribute)

        print 'Non mirror drive completion!!!',
