Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the directory where this script is located
scriptPath = fso.GetParentFolderName(WScript.ScriptFullName)
batFile = scriptPath & "\launch_gui_silent.bat"

' Check if the batch file exists
If fso.FileExists(batFile) Then
    WshShell.Run Chr(34) & batFile & Chr(34), 0, False
Else
    MsgBox "Error: launch_gui_silent.bat not found!" & vbCrLf & "Expected at: " & batFile, vbCritical, "Launch Error"
End If

Set fso = Nothing
Set WshShell = Nothing
