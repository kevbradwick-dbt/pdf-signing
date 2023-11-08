# PDF Signing Example

## Generate a p12 certificate

    openssl req -x509 -newkey rsa:4096 -keyout myKey.pem -out cert.pem -days 365 -nodes

    openssl pkcs12 -export -out keyStore.p12 -inkey myKey.pem -in cert.pem
