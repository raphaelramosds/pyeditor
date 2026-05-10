.PHONY: start

start:
	@cd pyeditor && python app.py

deploy:
	@pyinstaller --name "Pyeditor" --onefile --windowed pyeditor/app.py

clean:
	@rm -rf build/ dist/ app.spec