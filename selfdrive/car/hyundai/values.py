# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  STEER_MAX = 384   # 409 is the max, 255 is stock
  STEER_DELTA_UP = 4
  STEER_DELTA_DOWN = 7
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1


class CAR:
  #HYUNDAI
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  HYUNDAI_GENESIS = "HYUNDAI GENESIS 2015-2016"
  IONIQ_HEV = "HYUNDAI IONIQ HYBRID PREMIUM 2018-2020"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  KONA = "HYUNDAI KONA 2020"
  KONA_EV = "HYUNDAI KONA ELECTRIC 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_2019 = "HYUNDAI SONATA 2019"
  SONATA_HEV = "HYUNDAI SONATA HYBRID 2020"
  PALISADE = "HYUNDAI PALISADE 2020"
  GRANDEUR = "GRANDEUR IG 2017"
  GRANDEUR_HEV = "GRANDEUR IG HEV 2019"
  VELOSTER = "HYUNDAI VELOSTER 2019"

  # GENESIS
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G80 = "GENESIS G80 2017-2020"
  GENESIS_G90 = "GENESIS G90 2017-2020"

  # KIA
  KIA_FORTE = "KIA FORTE E 2018"
  KIA_OPTIMA = "KIA OPTIMA SX 2019 & 2016"
  KIA_OPTIMA_HEV = "KIA OPTIMA HYBRID 2017 & SPORTS 2019"
  KIA_SORENTO = "KIA SORENTO GT LINE 2018"
  KIA_STINGER = "KIA STINGER GT2 2018"
  KIA_NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  KIA_NIRO_HEV = "KIA NIRO HEV 2018"
  KIA_CEED = "KIA CEED 2019"
  KIA_SPORTAGE = "KIA SPORTAGE S 2020"
  KIA_CADENZA = "KIA K7 2016-2019"
  KIA_CADENZA_HEV = "KIA K7 HEV 2016-2019"
  
class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4

FINGERPRINTS = {
  CAR.ELANTRA: [{
    66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 897: 8, 832: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1170: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1345: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 2001: 8, 2003: 8, 2004: 8, 2009: 8, 2012: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.ELANTRA_GT_I30: [{
    66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1193: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1952: 8, 1960: 8, 1988: 8, 2000: 8, 2001: 8, 2004: 8, 2005: 8, 2008: 8, 2009: 8, 2012: 8, 2013: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.HYUNDAI_GENESIS: [{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 912: 7, 916: 8, 1024: 2, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1268: 8, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1342: 6, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1437: 8, 1456: 4
  }],
  CAR.SANTA_FE: [{
   67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 764: 8, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1186: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8
  }],
  CAR.SONATA: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 545: 8, 546: 8, 547: 8, 548: 8, 549: 8, 550: 8, 576: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 8, 865: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 908: 8, 909: 8, 912: 7, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1089: 5, 1096: 8, 1107: 5, 1108: 8, 1114: 8, 1136: 8, 1145: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1184: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 8, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1330: 8, 1339: 8, 1342: 6, 1343: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1379: 8, 1384: 8, 1394: 8, 1407: 8, 1419: 8, 1427: 6, 1446: 8, 1456: 4, 1460: 8, 1470: 8, 1485: 8, 1504: 3, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.SONATA_HEV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 546: 8, 548: 8, 576: 8, 593: 8, 688: 6, 757: 2, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1102: 8, 1108: 8, 1114: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1173: 8, 1180: 8, 1184: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 8, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1330: 8, 1339: 8, 1342: 6, 1343: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1446: 8, 1448: 8, 1456: 4, 1460: 8, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.SONATA_2019: [{
    66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1397: 8, 1407: 8, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 2000: 8, 2001: 8, 2004: 8, 2005: 8, 2008: 8, 2009: 8, 2012: 8, 2013: 8, 2014: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.KIA_OPTIMA: [{
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 625: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 909: 8, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1186: 2, 1191: 2, 1236: 2, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1268: 8, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1371: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1492: 8, 1530: 8, 1532: 5, 1905: 8, 1913: 8, 1952: 8, 1960: 8, 1988: 8, 1996: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.KIA_SORENTO: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1384: 8, 1407: 8, 1411: 8, 1419: 8, 1425: 2, 1427: 6, 1444: 8, 1456: 4, 1470: 8, 1489: 1
  }],
  CAR.KIA_STINGER: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_G70: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832:8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1168: 7, 1170: 8, 1173:8, 1184: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1419:8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.GENESIS_G80: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1024:2,  1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 8,  1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1437: 8, 1456: 4, 1470: 8
  }],
  CAR.GENESIS_G90: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2003: 8, 2004: 8, 2005: 8, 2008: 8, 2011: 8, 2012: 8, 2013: 8
  }],
  CAR.IONIQ_EV_LTD: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 7, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1425: 2, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1507: 8, 1535: 8
  }],
  CAR.IONIQ_HEV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 524: 8, 544: 7, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1164: 8, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1379: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2005: 8, 2008: 8, 2012: 8, 2013: 8
  },
  {
    68:8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 524: 8, 544: 8, 576:8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1164: 8, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1379: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1473: 8, 1476: 8, 1507: 8, 1535: 8, 1988: 8, 1996: 8, 2000: 8, 2004: 8, 2005: 8, 2008: 8, 2012: 8, 2013: 8
  }],
  CAR.KONA: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 354: 3, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832 : 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1193: 8, 1265: 4,1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 8, 1384: 8, 1394: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1996: 8, 2000: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8
  }],
  CAR.KONA_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 546: 8, 547: 8, 548: 8, 549: 8, 576: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1138: 4, 1151: 6, 1155: 8, 1157: 4, 1164: 8, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1193: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1378: 8, 1379: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.KONA_EV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 549: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1193: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1307: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1378: 4, 1379: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8
  }],
  CAR.KIA_FORTE: [{ # no SCC msgs in this string
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1078: 4, 1107: 5, 1136: 8, 1156: 8, 1170: 8, 1173: 8, 1191: 2, 1225: 8, 1265: 4, 1280: 4, 1287: 4, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1394: 8, 1407: 8, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.KIA_OPTIMA_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 6, 909: 8, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1168: 7, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1236: 2, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1420: 8, 1425: 2, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.PALISADE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 549: 8, 576: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1123: 8, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 8, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 2000: 8, 2004: 8, 2005: 8, 2008: 8, 2012: 8
  }],
  CAR.VELOSTER: [{
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 558: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1170: 8, 1181: 5, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1378: 4, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 1872: 8, 1988: 8, 1996: 8, 2000: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.GRANDEUR: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 547: 8, 549: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6 , 1456: 4, 1470: 8
  }],
  CAR.GRANDEUR_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 516: 8, 544: 8, 546: 8, 576: 8, 593: 8, 688: 5, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1108: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1173: 8, 1180: 8, 1185: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.KIA_SPORTAGE: [{ # no SCC msgs in this string
    67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 909: 8, 916: 8, 1040: 8, 1078: 4, 1170: 8, 1191: 2, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1419: 8, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1492: 8, 1530: 8
  }],
  CAR.KIA_NIRO_EV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 516: 8, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1193: 8, 1225: 8, 1260: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8, 1990: 8, 1998: 8, 1996: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.KIA_NIRO_HEV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1535: 8
  }], 
  CAR.KIA_CEED: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 354: 3, 356: 4, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1157: 4, 1168: 7, 1170: 8, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1394: 8, 1407: 8, 1414: 3, 1427: 6, 1456: 4, 2015: 8
  }],
  CAR.KIA_CADENZA: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1444: 8, 1456: 4, 1470: 8
  }],  
  CAR.KIA_CADENZA_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1096: 8, 1102: 8, 1108: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1210: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1343: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1379: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

# Don't use these fingerprints for fingerprinting, they are still used for ECU detection
IGNORED_FINGERPRINTS = []

FW_VERSIONS = {
  CAR.SONATA: {
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
    ],
  },
  CAR.SONATA_HEV: {
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310-L5500\xf1\x00DN8 MDPS C 1.00 1.02 56310-L5500 4DNHC102\xf1\xa01.02',
    ],
  },
  CAR.SANTA_FE: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00'],
  },
  CAR.KIA_STINGER: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104'],
  },
  CAR.KIA_OPTIMA_HEV: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
  },
  CAR.PALISADE: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',],
  },
  CAR.VELOSTER: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00JSL MDPS C 1.00 1.03 56340-J3000 8308', ],
  },
  CAR.KIA_NIRO_EV: {
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
    ],
  },
  CAR.KONA_EV: {
    (Ecu.eps, 0x7D4, None): [b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4000\x00 4OEDC104'],
  },
  CAR.IONIQ_HEV: {
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00AE  MDPS C 1.00 1.07 56310/G2301 4AEHC107',
      b'\xf1\x00AE  MDPS C 1.00 1.01 56310/G2310 4APHC101',
    ],
  },
  CAR.GENESIS_G70: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00IK  MDPS R 1.00 1.06 57700-G9420 4I4VL106', ],
  },
  CAR.KONA: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310J9030\x00 4OSDC105', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310/J9030 4OSDC105', ],
  },
  CAR.KIA_OPTIMA: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.engine, 0x7e0, None): [b'\x01TJFAJNU06F201H03'],
  }
}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.SONATA_HEV, CAR.PALISADE],
  "6B": [CAR.KIA_SORENTO, CAR.HYUNDAI_GENESIS],
}

FEATURES = {
  # which message has the gear
  "use_cluster_gears": set([CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.KIA_CADENZA, CAR.KIA_NIRO_HEV, CAR.GRANDEUR]),
  "use_tcu_gears": set([CAR.KIA_OPTIMA, CAR.SONATA_2019, CAR.VELOSTER]),
  "use_elect_gears": set([CAR.KIA_OPTIMA_HEV, CAR.SONATA_HEV, CAR.IONIQ_EV_LTD, CAR.IONIQ_HEV, CAR.KONA_EV, CAR.KIA_NIRO_EV, CAR.KIA_CADENZA_HEV,
                      CAR.GRANDEUR_HEV, CAR.KIA_NIRO_HEV, CAR.KONA_HEV]),

  # send LFA MFA message for new HKG models
  "send_lfa_mfa": set([CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SANTA_FE, CAR.KIA_NIRO_EV, CAR.KONA_EV, CAR.KONA,
                       CAR.KONA_HEV, CAR.IONIQ_HEV, CAR.IONIQ_EV_LTD]),
  # these cars use the FCA11 message for the AEB and FCW signals, all others use SCC12
  "use_fca": set([CAR.SONATA, CAR.SONATA_HEV, CAR.ELANTRA, CAR.ELANTRA_GT_I30, CAR.KIA_STINGER, CAR.KONA, CAR.KONA_EV,
              CAR.KIA_FORTE, CAR.KIA_OPTIMA, CAR.KIA_OPTIMA_HEV, CAR.KIA_NIRO_EV, CAR.KIA_CEED, CAR.KIA_CADENZA_HEV,
              CAR.KIA_SPORTAGE, CAR.KONA_HEV, CAR.PALISADE, CAR.GRANDEUR_HEV, CAR.GENESIS_G70, CAR.VELOSTER]),

  "use_bsm": set([CAR.SONATA, CAR.PALISADE, CAR.HYUNDAI_GENESIS, CAR.GENESIS_G70, CAR.GENESIS_G80, CAR.GENESIS_G90, CAR.KONA]),
  "allow_high_steer": set([CAR.KONA, CAR.KONA_EV, CAR.KONA_HEV]),
}

ELEC_VEH = set([CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.KIA_NIRO_EV])

HYBRID_VEH = set([CAR.KIA_OPTIMA_HEV, CAR.SONATA_HEV, CAR.IONIQ_HEV, CAR.KIA_CADENZA_HEV, CAR.GRANDEUR_HEV, CAR.KIA_NIRO_HEV, CAR.KONA_HEV])

DBC = {
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  CAR.HYUNDAI_GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SONATA_2019: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.VELOSTER: dbc_dict('hyundai_kia_generic', None),

  CAR.KIA_FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_OPTIMA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.KIA_SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_SPORTAGE: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CEED: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_NIRO_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.KIA_CADENZA: dbc_dict('hyundai_kia_generic', None),
  CAR.KIA_CADENZA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
}

STEER_THRESHOLD = 150
