wget http://archive.ubuntu.com/ubuntu/pool/main/libj/libjpeg-turbo/libjpeg-turbo8_2.0.3-0ubuntu1_amd64.deb
wget http://archive.ubuntu.com/ubuntu/pool/main/f/fontconfig/libfontconfig1_2.13.1-2ubuntu3_amd64.deb
wget http://archive.ubuntu.com/ubuntu/pool/main/libx/libxext/libxext6_1.3.4-0ubuntu1_amd64.deb
wget http://archive.ubuntu.com/ubuntu/pool/main/libx/libxrender/libxrender1_0.9.10-1_amd64.deb
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl3_3.0.2-0ubuntu1_amd64.deb


# Create directories for libraries
mkdir -p lib
mkdir -p usr/lib/x86_64-linux-gnu

# Extract the downloaded packages
dpkg-deb -x libjpeg-turbo8_2.0.3-0ubuntu1_amd64.deb .
dpkg-deb -x libfontconfig1_2.13.1-2ubuntu3_amd64.deb .
dpkg-deb -x libxext6_1.3.4-0ubuntu1_amd64.deb .
dpkg-deb -x libxrender1_0.9.10-1_amd64.deb .
dpkg-deb -x libssl3_3.0.2-0ubuntu1_amd64.deb .

mv usr/lib/x86_64-linux-gnu/* lib/
