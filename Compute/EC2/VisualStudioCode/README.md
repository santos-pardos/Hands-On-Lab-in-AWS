### Links
https://dev.to/aws-builders/running-vs-code-server-on-aws-51h6



curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz

tar -xf vscode_cli.tar.gz

~/code  tunnel --accept-server-license-terms --name vscode-santos