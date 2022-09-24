{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5723fcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Main app page (sets up navigation and routing)\n",
    "\n",
    "import streamlit as st\n",
    "from multiapp import MultiApp\n",
    "from components import url_summarize, web_summarize\n",
    "\n",
    "# Set up MultiApp feature (allows for multiple pages)\n",
    "app = MultiApp()\n",
    "\n",
    "st.set_page_config(page_title=\"Article AI\", page_icon=\"📝\", layout='centered', initial_sidebar_state=\"expanded\")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "# Article AI ◉\n",
    "Use Natural Language Processing to query articles and **produce brief summaries**\n",
    "\"\"\")\n",
    "\n",
    "st.markdown('----')\n",
    "\n",
    "# Other pages\n",
    "app.add_app(\"Via Search Term\", web_summarize.app)\n",
    "app.add_app(\"Via URL\", url_summarize.app)\n",
    "\n",
    "# The main app\n",
    "app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
