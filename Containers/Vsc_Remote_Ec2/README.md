## Visual Studio Code - SSH Remote EC2
```
Install SSH Remote Plug-in (Microsoft)
```
```
Remote-SSH:Open Configuration File...
/users/santos/.ssh/config
```


```
Host aws-ec2
    HostName ec2-44-229-243-8.us-west-2.compute.amazonaws.com
    User ec2-user
    IdentityFile c:\Temp\labsuser.pem
```

```
Change permissions in the Labuser.pem and config files
(Linux chmod 400. Windows (remove all users, add the windows user)
```

## Links
```
https://medium.com/@christyjacob4/using-vscode-remotely-on-an-ec2-instance-7822c4032cff
```

## Video
```
https://www.youtube.com/watch?v=FJlEQi6XfSA&list=PLr35b7rSarzgZkujDzF26aAbO9fsXxRT0&index=2
```

