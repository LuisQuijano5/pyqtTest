import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 1000
    height: 1000
    title: "QML Label Example"
    color: "#918D92"

    Rectangle{
        id: titleContainer

        //POSITIONING
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 25

        //SIZE
        width: parent.width
        height: title.implicitHeight + subtitle.implicitHeight + 25

        color: "#333333"

        Text {
            id: title
            text: "PyQT framework"
            font.pixelSize: 50
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
            color: "#FFFFFF"
            font.weight: 700
        }

        Text {
            id: subtitle
            text: "v: PyQt6"
            font.pixelSize: 30
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: title.bottom
            color: "#FFFFFF"
        }
    }

    Rectangle{
        id: infoContainer

        anchors.top: titleContainer.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 100

        width: infoTitle.implicitWidth + 50
        height: infoTitle.implicitHeight + namesList.implicitHeight + 200

        color: "#dddddd"
        border.color: "#000000"
        border.width: 2
        // border.radius doesn't exist as such, use radius instead
        radius: 10

        Text{
            id: infoTitle
            text: "GUIs Investigation - TAP"
            font.pixelSize: 35
            font.weight: 600
            anchors.topMargin: 25
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
        }

        ListView {
            id: namesList
            anchors.top: infoTitle.bottom
            anchors.topMargin: 25
            anchors.leftMargin: 25

            width: 200
            height: 200

            //define the elements needed
            model: ListModel {
                ListElement { name: "Emilio Sebastián Chavez Vega" }
                ListElement { name: "Ulises Andrade Gonzalez" }
                ListElement { name: "Luis Angel Quijano Guerrero" }
                ListElement { name: "Erick Martín Morín Lopez" }
            }

            //config of how each element appears, in this case it appears as a row
            delegate: Row {
                Text {
                    text: "    - "
                    font.pixelSize: 25
                    font.weight: 600
                }
                Text {
                    text: model.name
                    font.pixelSize: 25
                    font.weight: 600
                }
            }
        }
    }

}
