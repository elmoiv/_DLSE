
reg_data = '''Windows Registry Editor Version 5.00

; Add to Context Menu
[HKEY_CURRENT_USER\Software\Classes\SystemFileAssociations\.dlse\shell\DLSE]
@="Load with DLSE"
[HKEY_CURRENT_USER\Software\Classes\SystemFileAssociations\.dlse\shell\DLSE\command]
@="\\"{0}\\" \\"%1\\""
[HKEY_CURRENT_USER\Software\Classes\SystemFileAssociations\.dlse\shell\DLSE]
"Icon"="{0},0"

; Edit File Type Description
[HKEY_CURRENT_USER\Software\Classes\Applications\DLSE.exe]
@="DLSE Profile"
[HKEY_CURRENT_USER\Software\Classes\Applications\DLSE.exe]
"FriendlyTypeName"="DLSE Profile"

; Edit File Type Icon
[HKEY_CURRENT_USER\Software\Classes\Applications\DLSE.exe\DefaultIcon]
@="{0}.ico"
'''

def register_context_menu(path):
    with open('dlse.reg', 'w') as reg:
        reg.write(
            reg_data.format(
                path.replace('\\', '\\\\')
                )
            )