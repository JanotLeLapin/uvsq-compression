{ python3
, python311Packages
, mkShell
}: mkShell {
  packages = [
    python3
    python311Packages.python-lsp-server python311Packages.numpy python311Packages.pillow python311Packages.scipy
  ];
}
