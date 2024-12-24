from flask import Flask, jsonify, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the WebUI frontend

@app.route('/api/createSubscriber', methods=['POST'])
def create_subscriber():
    # Get subscriber data from the request
    data = request.json
    imsi = data.get('imsi')
    subscriber_key = data.get('subscriberKey')
    operator_key = data.get('operatorKey')
    amf = data.get('amf')
    ue_ambr_downlink = f"{data.get('ueAmbrDownlink')} {data.get('downlinkUnit')}"
    ue_ambr_uplink = f"{data.get('ueAmbrUplink')} {data.get('uplinkUnit')}"

    # Log subscriber data (this is where you can also add it to MongoDB)
    print(f"Subscriber Created: IMSI={imsi}, Downlink={ue_ambr_downlink}, Uplink={ue_ambr_uplink}")

    # Trigger a ping test after adding the subscriber
    ping_output = ping_test(destination="8.8.8.8")  # Replace with your destination IP or URL

    # Return both the subscriber creation response and ping results
    return jsonify({
        "message": f"Subscriber with IMSI {imsi} created successfully!",
        "ping_results": ping_output
    })

def ping_test(destination):
    """Function to perform a ping test to the specified destination."""
    try:
        # Run the ping command
        result = subprocess.run(
            ["ping", "-c", "4", destination],  # Ping 4 packets
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Return the ping output
        if result.returncode == 0:
            return {
                "success": True,
                "output": result.stdout
            }
        else:
            return {
                "success": False,
                "error": result.stderr
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
