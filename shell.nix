{ python3
, python311Packages
, mkShell
}: mkShell {
  packages = [
    python3
    python311Packages.tkinter python311Packages.python-lsp-server
  ];
}
