<powershell> 

# Install IIS
Import-Module ServerManager; 
Install-WindowsFeature web-server, web-webserver -IncludeAllSubFeature; 
Install-WindowsFeature web-mgmt-tools; 

# Install Static Website
Start-Sleep -Seconds 120;
Remove-item -recurse c:\inetpub\wwwroot\*; 
(New-Object System.Net.WebClient).DownloadFile("https://sanvalero-static-webs.s3.eu-west-1.amazonaws.com/Drink-Water.zip", "c:\inetpub\wwwroot\Drink-Water.zip"); 
Start-Sleep -Seconds 10;
Expand-Archive -Path "c:\inetpub\wwwroot\Drink-Water.zip" -DestinationPath "c:\inetpub\wwwroot" -Force;

</powershell>
