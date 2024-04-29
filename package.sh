pyinstaller --name 'Enscape Patcher' \
            --onefile \
            --console \
            --osx-bundle-identifier com.patch.enscape \
            --log-level=ERROR \
            app.py