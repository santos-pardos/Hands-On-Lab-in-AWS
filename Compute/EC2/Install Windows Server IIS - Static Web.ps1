'''
<powershell> 
# Install IIS
Import-Module ServerManager; 
Install-WindowsFeature web-server, web-webserver -IncludeAllSubFeature; 
Install-WindowsFeature web-mgmt-tools; 
# Install Static Website
Start-Sleep -Seconds 300;
Remove-item -recurse c:\inetpub\wwwroot\*; 
(New-Object System.Net.WebClient).DownloadFile("https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/Drink-Water.zip", "c:\inetpub\wwwroot\Drink-Water.zip"); 
Start-Sleep -Seconds 10;
Expand-Archive -Path "c:\inetpub\wwwroot\Drink-Water.zip" -DestinationPath "c:\inetpub\wwwroot" -Force;
</powershell>
'''

'''
<powershell>
# Installing web server
Install-WindowsFeature -name Web-Server -IncludeManagementTools
# Getting website code
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-EDCOMP-1-DEV/lab-01-ec2/code.zip -outfile "C:\Users\Administrator\Downloads\code.zip"
# Unzipping website code
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip
{
    param([string]$zipfile, [string]$outpath)
    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}
Unzip "C:\Users\Administrator\Downloads\code.zip" "C:\inetpub\"
# Setting Administrator password
$Secure_String_Pwd = ConvertTo-SecureString "P@ssW0rD!" -AsPlainText -Force
$UserAccount = Get-LocalUser -Name "Administrator"
$UserAccount | Set-LocalUser -Password $Secure_String_Pwd
</powershell>
'''
