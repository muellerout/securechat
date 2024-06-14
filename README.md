# Securechat

Securechar checks on communication channels for possible sensitive data leaks. Its first version uses only Slack yet.

## Built with

Django - admin panel is used to manage regular expressions and to monitor detected data leaks.

SQLite - database.

Celery - distributed task queue, used to perform background checks for data leaks.

Redis - message broker and result backend for celery.

Slack API - for deleting messages containing detected data leaks.

Ngrok - for forwarding traffic from Slack Events API to localhost, if you don't have a public endpoint that could receive webhooks.

## Requirements

### Ngrok

1. Create a free [ngrok account](https://dashboard.ngrok.com/signup).

2. In the ngrok dashboard, go to **Domains** and create a domain. You will need it later.

### Slack

1. Create a [Slack workspace](https://slack.com/get-started#/createnew). 

2. Create a [Slack app](https://api.slack.com/apps) binding the just created workspace to it.

3. In your slack app's control panel, go to **OAuth & Permissions** and add the OAuth scope `chat:write` to *User Token Scopes*.

4. Go to **Basic Information** and click `Install to Workspace`.

5. You will be requested for permissions. Click `Allow`. 

Your slack app is installed!

### ngrok.yaml

1. In the ngrok dashboard, go to **Your Authtoken**. Copy the token.

2. Open `ngrok.yaml` file in the project and paste your copied token into `authtoken` field. 

3. Go back to the ngrok dashboard and copy your ngrok domain into `domain` field in the `ngrok.yaml` as well.

Ngrok is ready to go!

### docker-compose.yaml

1. Append your ngrok domain to `ALLOWED_HOSTS` environment variable in `docker-compose.yaml` file.

2. Open your slack app's control panel and go to **OAuth & Permissions**.

3. Copy your user OAuth token.

4. Paste the token to `SLACK_API_TOKEN` environment variable in the `docker-compose.yaml`.

5. Generate a secret key with your favorite hashing algorithm and insert it to `SECRET_KEY` environment variable in the same `docker-compose.yaml` file.

Docker compose is configured!

### Running 

1. In the project folder, run `docker compose up`

2. Once you got the server up and running, open your slack app's control panel and go to **Event subscriptions**.

3. Enable events and copy your ngrok domain in the *Request URL* field as follows `https://<your-ngrok-domain>/slack/`. You should see *Verified* if you everything went smooth.

4. In the *Subscribe to events on behalf of users* section, add a workspace event `message.channels`. This event allows Slack Events API to send you a webhook request if a message is posted to any channel in the slack app's workspace.

## How to use securechat

Now you can open django admin panel per `127.0.0.1:8000/admin/` in your browser and create some regular expressions (*Regex*) incoming slack messages will be tested against. *Entry* field is regular expression itself. *Description* field is self-explained, just write what your regular expression should match.

If an incoming slack message contains the data leaks that the added regular expressions match, the message will be saved to the database, so you can view it and the corresponding regular expression in the django admin panel (*Data leaks*).

After saving to the database, message will be automatically deleted from the channel.

### Example:

Type `.*(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}.*` in the *Entry* field of the *Regex* model and `To match Maestro cards` in the *Description* field. 
Save it. Then go to one of your workspace channels and type `6759649826438453` or `676100041090`. 

Once you typed the message in the chat, it should be deleted and you should be able to see it in the *Data leaks*.