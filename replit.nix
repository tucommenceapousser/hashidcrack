{pkgs}: {
  deps = [
    pkgs.xsimd
    pkgs.pkg-config
    pkgs.libxcrypt
    pkgs.libcxx
    pkgs.arrow-cpp
    pkgs.wget
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
  ];
}
