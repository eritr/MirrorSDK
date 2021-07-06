# This Python file uses the following encoding: utf-8
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: E:/Documents/maya/2018/scripts\MirrorSDK.py
# Compiled at: 2018-06-18 08:42:33

# Use to start
# import MirrorSDKCustom
# MirrorSDKCustom.MirrorSDKUICustom()


import pymel.core as pm
import maya.cmds as mc
import sys


def MirrorSDKUICustom():
    TitleWindow = 'MirrorSDK_Custom'
    if pm.window(TitleWindow, q=True, ex=True):
        pm.deleteUI(TitleWindow)
    pm.window(TitleWindow)
    pm.showWindow()
    pm.columnLayout(adj=True)
    pm.text(l=TitleWindow, bgc=(0.1, 0.5, 0.5))
    pm.separator(st=None, h=5)
    pm.text(l='Find and replace L to R by template',
            bgc=(0.1, 0.1, 0.1), nbg=True)
    pm.textFieldGrp('search', l='Template:', tx='_L')
    pm.separator(st=None, h=5)
    pm.text(l="Fix controller's behavior (change sign)",
            bgc=(0.1, 0.1, 0.1))
    pm.checkBoxGrp('checkbox4', ncb=3, l='Translate Axis:',
                   la3=('X', 'Y', 'Z'))
    pm.checkBoxGrp('checkbox5', ncb=3, l='Rotate Axis:',
                   la3=('X', 'Y', 'Z'))
    pm.text(l="Fix driven objects' behavior (change sign)",
            bgc=(0.1, 0.1, 0.1))
    pm.checkBoxGrp('checkbox2', ncb=3, l='Translate Axis:',
                   la3=('X', 'Y', 'Z'))
    pm.checkBoxGrp('checkbox3', ncb=3, l='Rotate Axis:', la3=('X', 'Y', 'Z'))

    pm.textFieldButtonGrp('getCtrlgrp1', l='Driven Objects',
                          bl='Get selected', bc=getCtrlgrp1c)
    pm.separator(st=None, h=5)
    pm.button('button1', l='* Magic Button *', c=SDK3, bgc=(0.0, 0.3, 0.1))
    pm.separator(st=None, h=10)
    pm.text(l="Aleksei Sablin's modification, 2021/07/05",
            nbg=True)
    return


def getCtrl1c():
    getCtrl1c_list = pm.ls(sl=True)
    if len(getCtrl1c_list) > 1:
        pm.error('Only one object can be selected')
    pm.textFieldButtonGrp('getCtrl', e=True, tx=getCtrl1c_list[0])


def getCtrlgrp1c():
    pm.textFieldButtonGrp('getCtrlgrp1', e=True, tx=(',').join(mc.ls(sl=True)))


def SDK3(*args):

    text_field_of_list_driven_elems = pm.textFieldButtonGrp(
        'getCtrlgrp1', q=True, tx=True)

    text_field_of_list_driven_elems = text_field_of_list_driven_elems.split(
        ',')

    driver_attribute_invertation = - \
        1 if pm.checkBoxGrp('checkbox4', q=True, v1=True) else 1

    text_from_search_field = pm.textFieldGrp('search', q=True, tx=True)

    l2r_or_r2l_replacer = text_from_search_field.replace('L', 'R') if ('_L_').find(
        text_from_search_field) >= 0 else text_from_search_field.replace('R', 'L')

    for elem_from_text_field_of_list_driven_elems in text_field_of_list_driven_elems:
        drivens = pm.setDrivenKeyframe(elem_from_text_field_of_list_driven_elems,
                                       dn=True, q=True)

        # TODO: написать проверку

        for driven in drivens:
            # READING...
            mirrored_driven = driven.replace(text_from_search_field, l2r_or_r2l_replacer) if driven.find(
                text_from_search_field) >= 0 else driven.replace(l2r_or_r2l_replacer, text_from_search_field)
            print('*** NEW DRIVEN ***')
            # Get the driver values
            driverValues = pm.keyframe(driven, q=True, floatChange=True)
            print("driverValues", driverValues)
            # Get the driven values
            drivenValues = pm.keyframe(driven, q=True, valueChange=True)
            print("drivenValues", drivenValues)
            # Get the in tangents and out tangents
            inTangents = pm.keyTangent(driven, q=True, itt=True)
            print("inTangents", inTangents)
            outTangents = pm.keyTangent(driven, q=True, ott=True)
            print("outTangents", outTangents)
            # Get pre and post infinity types for this attribute
            infinity = pm.setInfinity(driven, q=True, pri=True, poi=True)
            print("infinity", infinity)

            # WRITTING...
            # For every driven value...
            for i in range(len(drivenValues)):
                driverList = pm.setDrivenKeyframe(driven, q=True, cd=True)
                mirrored_driver = driverList[0].replace(text_from_search_field, l2r_or_r2l_replacer) if driverList[0].find(
                    text_from_search_field) >= 0 else driverList[0].replace(l2r_or_r2l_replacer, text_from_search_field)

                tmpDR = mirrored_driver.split('.')
                attr = tmpDR[len(tmpDR) - 1]
                mirDR = 1

                if attr == 'translateX':
                    mirDR = - \
                        1 if pm.checkBoxGrp(
                            'checkbox4', q=True, v1=True) else 1

                elif attr == 'translateY':
                    mirDR = - \
                        1 if pm.checkBoxGrp(
                            'checkbox4', q=True, v2=True) else 1

                elif attr == 'translateZ':
                    mirDR = - \
                        1 if pm.checkBoxGrp(
                            'checkbox4', q=True, v3=True) else 1

                elif attr == 'rotateX':
                    mirDR = - \
                        1 if pm.checkBoxGrp(
                            'checkbox5', q=True, v1=True) else 1

                elif attr == 'rotateY':
                    mirDR = - \
                        1 if pm.checkBoxGrp(
                            'checkbox5', q=True, v2=True) else 1

                elif attr == 'rotateZ':
                    mirDR = - \
                        1 if pm.checkBoxGrp(
                            'checkbox5', q=True, v3=True) else 1

                print("mirrored_driver", mirrored_driver)
                print("mirDR", mirDR)
                pm.setAttr(mirrored_driver, driverValues[i]*mirDR)

                tmpDN = mirrored_driven.split('.')
                attr = tmpDN[len(tmpDN) - 1]
                mirDN = 1

                if attr == 'translateX':
                    mirDN = - \
                        1 if pm.checkBoxGrp(
                            'checkbox2', q=True, v1=True) else 1

                elif attr == 'translateY':
                    mirDN = - \
                        1 if pm.checkBoxGrp(
                            'checkbox2', q=True, v2=True) else 1

                elif attr == 'translateZ':
                    mirDN = - \
                        1 if pm.checkBoxGrp(
                            'checkbox2', q=True, v3=True) else 1

                elif attr == 'rotateX':
                    mirDN = - \
                        1 if pm.checkBoxGrp(
                            'checkbox3', q=True, v1=True) else 1

                elif attr == 'rotateY':
                    mirDN = - \
                        1 if pm.checkBoxGrp(
                            'checkbox3', q=True, v2=True) else 1

                elif attr == 'rotateZ':
                    mirDN = - \
                        1 if pm.checkBoxGrp(
                            'checkbox3', q=True, v3=True) else 1

                pm.setAttr(mirrored_driven, drivenValues[i]*mirDN)
                pm.setDrivenKeyframe(
                    mirrored_driven, cd=mirrored_driver, ott=outTangents[i], itt=inTangents[i])
                pm.setInfinity(mirrored_driven,
                               pri=infinity[0], poi=infinity[1])
