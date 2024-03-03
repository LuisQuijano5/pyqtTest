import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 1000
    height: 1000
    title: "QML Label Example"

    // Label element
    Text {
        id: myLabel
        text: "Hello, World!"
        font.pixelSize: 24
        anchors.centerIn: parent
    }

    Text {
        id: myLabel2
        text: "goooool"
        font.pixelSize: 24
    }
}
