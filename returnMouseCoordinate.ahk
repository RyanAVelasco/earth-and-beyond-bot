ScrollLock::reload

`::
loop, {
    MouseGetPos, x, y
    ToolTip, %x% and %y%, x, y
    sleep, 1000
}