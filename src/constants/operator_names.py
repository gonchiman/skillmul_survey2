from enum import Enum


class OperatorNames(Enum):
    LIFENG = "lifeng"
    ROSSI = "rossi"
    ENDMINISTRATOR = "endministrator"
    CHEN_QIANYU = "chen_qianyu"
    ESTELLA = "estella"
    POGRANICHNIK = "pogranichnik"
    ALESH = "alesh"
    ARCLIGHT = "arclight"
    AKEKURI = "akekuri"
    EMBER = "ember"
    SNOWSHINE = "snowshine"
    CATCHER = "catcher"
    TANGTANG = "tangtang"
    PERLICA = "perlica"
    WULFGARD = "wulfgard"
    FLUORITE = "fluorite"
    YVONNE = "yvonne"
    LAEVATAIN = "laevatain"
    LASTRITE = "lastrite"
    AVYWENNA = "avywenna"
    DA_PAN = "da_pan"
    GILBARTA = "gilbarta"
    ARDELIA = "ardelia"
    XAIHI = "xaihi"
    ANTAL = "antal"

# 識別子ルール:
# 基本はオペレーター名の先頭2文字を大文字にする。
# 既存の識別子と被る場合は、後から実装したオペレーター側を変更する。
# 実装順が同じ場合は、レアリティが低い方を変更する。
# 例: rossi -> RO が被る場合、RS に変更する。
OPERATOR_IDENTIFIERS = {
    OperatorNames.LIFENG: "LI",
    OperatorNames.ROSSI: "RO",
    OperatorNames.ENDMINISTRATOR: "EN",
    OperatorNames.CHEN_QIANYU: "CH",
    OperatorNames.ESTELLA: "ES",
    OperatorNames.POGRANICHNIK: "PO",
    OperatorNames.ALESH: "AL",
    OperatorNames.ARCLIGHT: "AC",
    OperatorNames.AKEKURI: "AK",
    OperatorNames.EMBER: "EM",
    OperatorNames.SNOWSHINE: "SN",
    OperatorNames.CATCHER: "CA",
    OperatorNames.TANGTANG: "TA",
    OperatorNames.PERLICA: "PE",
    OperatorNames.WULFGARD: "WU",
    OperatorNames.FLUORITE: "FL",
    OperatorNames.YVONNE: "YV",
    OperatorNames.LAEVATAIN: "LV",
    OperatorNames.LASTRITE: "LA",
    OperatorNames.AVYWENNA: "AV",
    OperatorNames.DA_PAN: "DA",
    OperatorNames.GILBARTA: "GI",
    OperatorNames.ARDELIA: "AR",
    OperatorNames.XAIHI: "XA",
    OperatorNames.ANTAL: "AN",
}