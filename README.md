# Build Applications with GitHub Copilot Agent Mode

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey Windphoenix2!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/Windphoenix2/skills-build-applications-w-copilot-agent-mode/issues/1)

---

# How to Start the OctoFit Tracker App

Follow these steps to start and verify the OctoFit Tracker app locally:

1. **Check if MongoDB server is running**
   - Run: `ps aux | grep mongod` (Linux/macOS) or check MongoDB service in Task Manager (Windows)
   - If not running, see next step.

2. **Start MongoDB server if not running**
   - On Linux/macOS: `sudo systemctl start mongod` or `mongod --config /usr/local/etc/mongod.conf`
   - On Windows: Start the MongoDB service from Services or run `mongod` in a terminal.

3. **Repair MongoDB server if it will not start**
   - Run: `mongod --repair` (ensure MongoDB is stopped first)
   - Check logs for errors and resolve disk space or permission issues if needed.

4. **Start MongoShell**
   - Run: `mongosh` to open the MongoDB shell and verify connection.

5. **Set environment variables (if needed)**
   - For Codespaces or remote: Set `REACT_APP_CODESPACE_NAME` in your environment or `.env` file for React to connect to the backend.

6. **Start the Django backend server**
   - Activate the Python virtual environment:
     - Windows: `octofit-tracker\backend\venv\Scripts\activate`
     - macOS/Linux: `source octofit-tracker/backend/venv/bin/activate`
   - Run: `python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000`

7. **Start the React app**
   - In a new terminal:
     - `cd octofit-tracker/frontend`
     - `npm start`
   - The app will open at http://localhost:3000

8. **Check the API in your browser**
   - Visit: http://localhost:8000/api/ to verify the Django REST API is running.

9. **Open the React app**
   - Visit: http://localhost:3000 to use the OctoFit Tracker frontend.

---

If you encounter issues, check the terminal output for errors and ensure all services are running.

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

